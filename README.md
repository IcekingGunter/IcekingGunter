- 👋 Hi, I’m @IcekingGunter
Im creating an app for the first time, im interested in accomplishing a couple of tasks with this app.  But firstly Ill start off by
saying what it is.  Its a discovery app, id like people who are interested in mushrooms to be able to pull out their phone
and by focusing the camera on the mushroom they find, let the app identify it, and then decide where they want to store the pins location
(gps coordinates)  the app leaves behind a pin on a map so you can see where you found the particular mushroom.
each mushroom is given a point 1-3 common uncommon rare, each carrying their own point system. 1,5,10.
You can choose to share your pins with either your friends, everyone or keep them private.
points vary based on region and availability of the mushroom in your particular region.
itd have an achievement system for kicks, and a leaderboard where itd showcase cool finds people send in.
the app would have to store pictures and the like so that people can see what others have found.
The app upon scanning the mushroom not only awards points, but tells you a summary of the mushroom, what genus and species it belongs to,
whether you can eat it, average life span, fruiting time, etc alot of details about the mushroom in quick bursts.  
I have sql knowledge and experience but ive never made an app so im looking for insights from those who know more than I and are willing to help me structure my app and build it.

Flask/
└── mycologyflask/
    ├── __init__.py  
    ├── models.py
    └── routes/
        ├── __init__.py
        └── mushrooms.py

MY **postgresql** database is structured like this:

Table name:  characteristics
Columns: id, mushroom_id, characteristic_name, value ,created_at

Table name: genus
Columns: id, name

Table name: mushroom
Columns: id, species_id, substrate_id, colonization_temp, avg_colonization_time, fruiting_temp, avg_fruiting_time, harvest_weight, color, shape, edibility, name, rarity, points

Table name: observations
Columns: id, user_id, mushroom_id, observation_date, location, notes, photo_url, created_at, temperature, weather_conditions, notes_tsvector, is_public, privacy_setting, is_private

Table name: spatial_ref_sys
Columns: srid, auth_name, auth_srid, srtext

Table name: species
Columns: id, genus_id, name

Table name: substrate
Columns: Sawdust, Wheat straw, Corncobs, Rye grain, Soybean hulls, Coffee grounds, Coconut coir, Wood chips, Paper waste, Manure

Table name: users
Columns: id, username, email, hashed_password, created_at, points
