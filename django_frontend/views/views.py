from django.shortcuts import render

ROOMS = [
    {"id": 1, "title": "Deluxe Suite", "price": 150, "type":"Suite", "capacity":2, "image_url":"/static/images/room1.jpg", "status":"Available"},
    {"id": 2, "title": "Executive Room", "price": 120, "type":"Standard","capacity":2, "image_url":"/static/images/room2.jpg", "status":"Occupied"},
    {"id": 3, "title": "Family Suite", "price": 200, "type":"Family","capacity":4, "image_url":"/static/images/room3.jpg", "status":"Available"},
    {"id": 4, "title": "Standard Room", "price": 89, "type":"Standard","capacity":2, "image_url":"/static/images/room2.jpg", "status":"Available"},
    {"id": 5, "title": "Premium Suite", "price": 250, "type":"Suite","capacity":2, "image_url":"/static/images/room1.jpg", "status":"Occupied"},
    {"id": 6, "title": "Studio Room", "price": 75, "type":"Standard","capacity":1, "image_url":"/static/images/room3.jpg", "status":"Available"},
]

BOOKINGS = [
    {"id":"#BK-1001","guest_name":"John Smith","room":"Deluxe Suite","checkin":"Dec 10, 2024","checkout":"Dec 15, 2024","status":"Confirmed","nights":5,"total":750},
    {"id":"#BK-1002","guest_name":"Emily Johnson","room":"Executive Room","checkin":"Dec 8, 2024","checkout":"Dec 10, 2024","status":"Pending","nights":2,"total":240},
    {"id":"#BK-1003","guest_name":"Michael Brown","room":"Family Suite","checkin":"Dec 12, 2024","checkout":"Dec 18, 2024","status":"Confirmed","nights":6,"total":1200},
    {"id":"#BK-1004","guest_name":"Sarah Davis","room":"Standard Room","checkin":"Dec 5, 2024","checkout":"Dec 7, 2024","status":"Cancelled","nights":2,"total":178},
    {"id":"#BK-1005","guest_name":"David Wilson","room":"Premium Suite","checkin":"Dec 20, 2024","checkout":"Dec 25, 2024","status":"Confirmed","nights":5,"total":1250},
]

def index(request):
    return render(request, 'index.html', {"rooms": ROOMS[:3], "testimonials": []})

def rooms(request):
    return render(request, 'rooms.html', {"rooms": ROOMS})

def room_details(request, room_id):
    room = next((r for r in ROOMS if r["id"] == int(room_id)), ROOMS[0])
    return render(request, 'room_details.html', {"room": room})

def booking(request):
    return render(request, 'booking.html', {"rooms": ROOMS})

def admin_dashboard(request):
    total_rooms = len(ROOMS)
    occupied_rooms = len([r for r in ROOMS if r.get("status") == "Occupied"])
    occupancy_rate = int((occupied_rooms / total_rooms * 100)) if total_rooms > 0 else 0
    
    total_bookings = len(BOOKINGS)
    total_revenue = sum([b["total"] for b in BOOKINGS])
    
    return render(request, 'admin_dashboard.html', {
        "total_rooms": total_rooms,
        "occupied_rooms": occupied_rooms,
        "occupancy_rate": occupancy_rate,
        "total_bookings": total_bookings,
        "total_revenue": total_revenue,
        "recent_bookings": BOOKINGS[:4],
    })

def admin_rooms(request):
    total_rooms = len(ROOMS)
    occupied_rooms = len([r for r in ROOMS if r.get("status") == "Occupied"])
    available_rooms = total_rooms - occupied_rooms
    
    return render(request, 'admin_rooms.html', {
        "rooms": ROOMS,
        "total_rooms": total_rooms,
        "occupied_rooms": occupied_rooms,
        "available_rooms": available_rooms,
    })

def admin_bookings(request):
    return render(request, 'admin_booking.html', {"bookings": BOOKINGS})
