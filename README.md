Team Name

Pheonix

Problem Statement

Critical medicines are not easily found during emergencies.
Patients and caregivers often waste valuable time searching for required medicines without knowing their availability nearby.

Our Solution

A smart platform that helps users quickly locate nearby pharmacies with available medicines, provides the fastest route to reach them, and alerts pharmacies in advance during emergencies.

Features
📍 Nearby Pharmacy Detection
💊 Real-time Medicine Availability
🗺️ Fastest Route Suggestion
🔔 Pharmacy Alert System
📱 User-Friendly Interface
⚡ Emergency Response Optimization
Components / Technologies Used
React.js / HTML / CSS (Frontend)
Node.js / Express or Flask (Backend)
MongoDB / Firebase (Database)
Google Maps API (Routing & Location)
Figma (UI/UX Design)
Team Members
Rahul Prakash Dhage
Suraj kurdekar
Sharan rathod
Status

Project Under Development 🚧

front end code

<!DOCTYPE html>
<html>
<head>
    <title>Medicine Availability</title>
</head>
<body>

<h1>🚑 Emergency Medicine Finder</h1>

<form action="/search" method="post">
    <input type="text" name="medicine" placeholder="Enter medicine name" required>
    <button type="submit">Search</button>
</form>

{% if results %}
    <h2>Results for "{{ query }}"</h2>
    <ul>
        {% for store in results %}
            <li>
                <strong>{{ store.name }}</strong><br>
                Location: {{ store.location }}<br>
                Phone: {{ store.phone }}
            </li>
        {% endfor %}
    </ul>
{% elif query %}
    <p>No stores found for "{{ query }}"</p>
{% endif %}

</body>
</html>
