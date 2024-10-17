# Delivery System (Cloud Kitchen) Like Zomato

List of nearby restaurants by gps location to order online only by App

Requirements:
- Search for restaurants
    - By type of cuisine
    - Specials (Those with current specials)
    - By rating
    - If they are pet friendly
    - If they are outdoors
    - If they are open now
    - If they offer alcohol
- Show photos of the restaurant
- Save rating
- Restaurant Reviews
- Menu
    - Select dishes
    - Pay online
    - Request address (find the closest and most active) <<< Focus on this part
        - Dividing the area by regions can help to find the nearest one.
	
	
## Delivery System
- Matching 
	- Time (ETA), Rating of Delivery Partner
- Tracking not Routing

Components:
Person --- Rider Manager (where is the rider?)

Restaurants  ------ Delivery Manager --- Rider Manager

Rider ---- Rider Manager --- Cache (<RiderId>, Location, Rating, NumOfDeliveriesOnThatDay) ---- NotificationService

Rider sending consistently the location to RiderManager by persistent connection

Considerations:
- Capacity Estimation (1 million deliveries (1 city), 100mil motociclistas)