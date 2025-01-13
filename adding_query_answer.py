

#I am at NIG Vienna. Show me the cheapest restaurants in reach of 15 minute walk.
q1 = { "task": [ "find_POI" ], "poi": { "type": "restaurant", "givenLocation": { "name": "NIG Vienna", "address": "Universitätsstraße 7, 1010 Vienna, Austria" }, "distance": { "value": 15, "unit": "minutes" }, "keywords": "", "open": True, "max_price": 1, "best_reviewed":False }}

#I need the fastet way through the 1. district from Karlsplatz to Schwedenplatz
q2 = { "task": [ "routing" ], "route": { "transportationMode": "walking", "startLocation": { "name": "Karlsplatz", "address": "Karlsplatz, Vienna" }, "endLocation": { "name": "Schwedenplatz", "address": "Schwedenplatz, Vienna" } } }

#Where is the best kaiserschmarrn in Vienna?
q3 = { "task": [ "find_POI" ], "poi": { "type": "restaurant", "givenLocation": { "name": "Vienna", "address": "Vienna, Austria" }, "distance": { "value": 5, "unit": "kilometers" }, "keywords": "kaiserschmarrn", "open": True, "max_price": 4, "best_reviewed": True } }

#I would like to have some ice cream. Which ice cream parlors in Vienna are still open in December?
q4 = { "task": [ "find_POI" ], "poi": { "type": "ice cream parlor", "givenLocation": { "name": "Vienna", "address": "Vienna, Austria" }, "distance": { "value": 5, "unit": "kilometers" }, "keywords": "ice cream", "open": True, "max_price": 4, "best_reviewed": True } }

#I'm meeting my friends at the Spittelberg Chirstmas Market. How long does it take to walk there from the main university?

q5 = { "task": [ "routing" ], "route": { "transportationMode": "walking", "startLocation": { "name": "main university", "address": "Universitätsring 1, 1010 Vienna, Austria" }, "endLocation": { "name": "Spittelberg Christmas Market", "address": "Spittelberggasse, 1070 Vienna, Austria" } } }

#I will be at the train station Ottakring tomorrow at 6pm. I want to buy beer and then go play football. What are my options?
###doesnt work!!
q6 = { "task": ["find_POI", "routing" ], "poi": { "type": "store", "givenLocation": { "name": "Ottakring Train Station", "address": "Ottakring, Vienna" }, "distance": { "value": 500, "unit": "meters" }, "keywords": "beer", "open": True, "max_price": 3, "best_reviewed": True }, "route": { "transportationMode": "walking", "startLocation": { "name": "Ottakring Train Station", "address": "Ottakring, Vienna" }, "endLocation": { "name": "nearest football field", "address": "to be determined" } } }


#I am currently at the vienna airport at terminal 1 and want to find a four star hotel in the city, which is close to Stadtpark. What are my options and which public transport can I take to get there?
#doenst really work
q7 = { "task": [ "find_POI", "routing" ], "poi": { "type": "hotel", "givenLocation": { "name": "Stadtpark", "address": "Parkring, 1010 Vienna, Austria" }, "distance": { "value": 1, "unit": "kilometers" }, "keywords": "four star", "open": True, "max_price": 4, "best_reviewed": True }, "route": { "transportationMode": "transit", "startLocation": { "name": "Vienna Airport Terminal 1", "address": "Wien-Flughafen, 1300 Schwechat, Austria" }, "endLocation": { "name": "Stadtpark", "address": "Parkring, 1010 Vienna, Austria" } } }

#I'ts already 11pm and I am standing at the NIG in Vienna. Where can i find something to eat closeby, say within a five minute walk?
q8 = { "task": [ "find_POI" ], "poi": { "type": "restaurant", "givenLocation": { "name": "NIG", "address": "Universitätsstraße 7, 1010 Vienna, Austria" }, "distance": { "value": 5, "unit": "minutes" }, "keywords": "food", "open": True, "max_price": 4, "best_reviewed": True } }

#"I am at the NIG Vienna. I need to go to Columbus Center by public transport. Is there a good cafe near by, where I can wait for a friend?"
q9 = { "task": [ "routing", "find_POI" ], "route": { "transportationMode": "transit", "startLocation": { "name": "NIG Vienna", "address": "Universitätsstraße 7, 1010 Vienna, Austria" }, "endLocation": { "name": "Columbus Center", "address": "Columbusplatz 7-8, 1100 Vienna, Austria" } }, "poi": { "type": "cafe", "givenLocation": { "name": "Columbus Center", "address": "Columbusplatz 7-8, 1100 Vienna, Austria" }, "distance": { "value": 500, "unit": "meters" }, "keywords": "coffee", "open": True, "max_price": 3, "best_reviewed": True } }

#"I want to visit Vienna with my family. Can you recommend the five best activities close to the center?"

q10 = { "task": [ "find_POI" ], "poi": { "type": "activity", "givenLocation": { "name": "Vienna city center", "address": "Vienna, Austria" }, "distance": { "value": 5, "unit": "kilometers" }, "keywords": "family-friendly", "open": True, "max_price": 3, "best_reviewed": True } }

#I want to go to an art gallery in vienna showcasing contemporary art. Preferably with late opening hours and accessible by public transport.

q11 = { "task": [ "find_POI", "routing" ], "poi": { "type": "art gallery", "givenLocation": { "name": "Vienna", "address": "Vienna, Austria" }, "distance": { "value": 30, "unit": "minutes" }, "keywords": "contemporary art", "open": True, "max_price": 4, "best_reviewed": True }, "route": { "transportationMode": "transit", "startLocation": { "name": "Current Location", "address": "Current Location" }, "endLocation": { "name": "Art Gallery", "address": "Vienna, Austria" } } }

#I'm standing in front of NIG and meet up with friends at Wien Simmering station, where we want to eat some japanese food. How can I get there with public transport, and what are the closest restaurants?

q12 = { "task": [ "routing", "find_POI" ], "route": { "transportationMode": "transit", "startLocation": { "name": "NIG", "address": "Universitätsstraße 7, 1010 Vienna, Austria" }, "endLocation": { "name": "Wien Simmering station", "address": "Simmeringer Hauptstraße, 1110 Vienna, Austria" } }, "poi": { "type": "restaurant", "givenLocation": { "name": "Wien Simmering station", "address": "Simmeringer Hauptstraße, 1110 Vienna, Austria" }, "distance": { "value": 500, "unit": "meters" }, "keywords": "Japanese", "open": True, "max_price": 4, "best_reviewed": True } }

#Can you show me the best sunset spots in vienna, which route will be the one with the best view and is there much incline?
#will not work

#I would like to find a gym for exercise near NIG or Thaliastraße, with a maximum monthly price of 80 Euros.
q14 = { "task": [ "find_POI" ], "poi": { "type": "gym", "givenLocation": { "name": "NIG", "address": "Universitätsstraße 7, 1010 Vienna, Austria" }, "distance": { "value": 2, "unit": "kilometers" }, "keywords": "exercise", "open": True, "max_price": 80, "best_reviewed": True } }

#I want to meet up with a friend. He lives near the subway station Simmering, and I live near the subway station Taborstraße. We want to meet up in a café somewhere in the middle. Where can we meet?
q15 = { "task": [ "find_POI" ], "poi": { "type": "café", "givenLocation": { "name": "between Simmering and Taborstraße", "address": "Vienna" }, "distance": { "value": 10, "unit": "minutes" }, "keywords": "coffee", "open": True, "max_price": 3, "best_reviewed": True } }

#I would like to sew myself a jacket and still need fabric. Where can I find fabric stores in Vienna?
q16 = { "task": [ "find_POI" ], "poi": { "type": "fabric store", "givenLocation": { "name": "Vienna", "address": "Vienna, Austria" }, "distance": { "value": 5, "unit": "kilometers" }, "keywords": "fabric", "open": True, "max_price": 4, "best_reviewed": True } }

#I'm currently at the NIG and would like to go out for a meal. Is there a restaurant that serves strictly vegetarian and vegan food within a 10 minute walk distance?
q17 = { "task": [ "find_POI" ], "poi": { "type": "restaurant", "givenLocation": { "name": "NIG", "address": "Universitätsstraße 7, 1010 Vienna, Austria" }, "distance": { "value": 10, "unit": "minutes" }, "keywords": "vegetarian, vegan", "open": True, "max_price": 4, "best_reviewed": True } } 

#It is Sunday and I forgot to buy flour. Can you show me all supermarkets in Vienna which are open on Sundays?
q18 = { "task": [ "find_POI" ], "poi": { "type": "supermarket", "givenLocation": { "name": "Vienna", "address": "Vienna, Austria" }, "distance": { "value": 5, "unit": "kilometers" }, "keywords": "flour", "open": True, "max_price": 3, "best_reviewed": False } }

#I want to go ice skating in Vienna. Where can I go on a Monday at 5 pm?
q19 = { "task": [ "find_POI" ], "poi": { "type": "ice skating rink", "givenLocation": { "name": "Vienna", "address": "Vienna, Austria" }, "distance": { "value": 10, "unit": "kilometers" }, "keywords": "ice skating", "open": True, "max_price": 4, "best_reviewed": True } }


#I want to have a picnic with my friends. We are at Gregor-Mendel House at BOKU and we want to walk a maximum of 15 minutes. What parks are there?
q20 = { "task": [ "find_POI" ], "poi": { "type": "park", "givenLocation": { "name": "Gregor-Mendel House at BOKU", "address": "Gregor-Mendel-Straße 33, 1180 Vienna, Austria" }, "distance": { "value": 15, "unit": "minutes" }, "keywords": "park", "open": True, "max_price": 0, "best_reviewed": False } }

import json 
import googlemaps 
import sys
import geocoder

# Google Maps API-Key
API_KEY = "AIzaSyBs0wTugH9xooZExAWERzdi27L4VUh5snE"
gmaps = googlemaps.Client(key=API_KEY)


def get_tasks(query):
    try:
        task_list = query["task"]
        return task_list
    #if no task in json, we stop
    except KeyError as e:
        print("No task was given in the JSON, stopping.")
        sys.exit(1)

def geocode_json(data):
    lat = 48
    lon = 16
    if "givenLocation" not in data:
        g = geocoder.ip("me")
        lat = g.latlng[0]
        lon = g.latlng[1]
        print("no loc given, using device-ip:")
        print(lat,lon)
    else:
        loc = data["givenLocation"]
        name = loc["name"] if "name" in loc else ""
        address = loc["address"] if "address" in loc else ""
        outLoc = name  + " " + address
        geocode_results = gmaps.geocode(outLoc)
        lat = geocode_results[0]["geometry"]["location"]["lat"]
        lon = geocode_results[0]["geometry"]["location"]["lng"]
    return lat,lon


#turns the answer of gmaps.places_nearby into something workable (geoJson)
#for places nearby collection of points
def gmaps_places_nearby_geojson(places_results):
    results = places_results["results"]
    geoJson = {"type": "FeatureCollection","features": []}
    for result in results:
        thisFeature = {"type": "Feature","geometry":{"type":"Point","coordinates":[0,0]},"properties":{}}
        thisFeature["geometry"]["coordinates"][0] = result["geometry"]["location"]["lng"]
        thisFeature["geometry"]["coordinates"][1] = result["geometry"]["location"]["lat"]
        thisFeature["properties"]["name"] = result["name"]
        thisFeature["properties"]["price_level"] = result["price_level"]
        thisFeature["properties"]["rating"] = result["rating"]
        thisFeature["properties"]["number_of_ratings"] = result["user_ratings_total"]
        thisFeature["properties"]["address"] = result["vicinity"]
        geoJson["features"].append(thisFeature)
    answer = ""
    i = 0
    for result in results: 
        if i == 0:
            answer += "We recommend you to go to "
        elif i%2==0:
            answer += ". You can also go to "
        else:
            answer += ". We also suggest "
        answer = answer + result["name"] + " which has a raiting of " + str(result["rating"]) + " and is located at " + result["vicinity"]
        i += 1
    answer += "."
    geoJson["answer"] = answer
    return geoJson

def find_poi(query):
    try:
        data = query["poi"]
        type_ = data["type"]
    except KeyError as e:
        print("Schema wrong, stopping.")
        sys.exit(1)
    lat,lon = geocode_json(data)
    dis_unit = data["distance"]["unit"] if "distance" in data else "meters"
    distance = data["distance"]["value"] if "distance" in data else 500
    if dis_unit == "kilometers":
        distance *= 1000
    #we still need to deal with this
    elif dis_unit == "minutes":
        distance *=85
    price_level = data["max_price"] if "max_price" in data else 4
    be_open = bool(data["open"]) if "open" in data else True
    our_keyword = data["keywords"] if "keywords" in data else ""
    places_results = gmaps.places_nearby((lat,lon),radius = distance,keyword=our_keyword, open_now=be_open,type=type_,max_price=price_level)
    if places_results["status"] == "ZERO_RESULTS":
        print("No suitable place found :(.")
        return {}
    geoJson = gmaps_places_nearby_geojson(places_results)
    #if we want the best we sort by rating
    if "best_reviewed" in data and data["best_reviewed"]:
        geoJson["features"].sort(reverse=True,key=(lambda x:x["properties"]["rating"]))
    #keep the first 10 results
    del geoJson["features"][10:]
    return geoJson

#turns the answer of gmaps.places_nearby into something workable (geoJson)
#for places nearby collection of points
def gmaps_routing_geojson(routing_result):
    step_list = routing_result["legs"][0]["steps"]
    geoJson = {"type": "FeatureCollection","features": []}
    linestring =  { "type": "Feature", "geometry": {"type": "LineString","coordinates": [] }, "properties": {}}
    for step in step_list:
        linestring["geometry"]["coordinates"].append([step["start_location"]["lng"],step["start_location"]["lat"]])
    #add the end point of last step
    linestring["geometry"]["coordinates"].append([step_list[-1]["end_location"]["lng"],step["end_location"]["lat"]])
    linestring["properties"]["duration"] = routing_result["legs"][0]["duration"]["text"]
    linestring["properties"]["distance"] = routing_result["legs"][0]["distance"]["text"]
    geoJson["features"].append(linestring)
    answer = "This route will take " + routing_result["legs"][0]["duration"]["text"] + " and is " + routing_result["legs"][0]["distance"]["text"] + " long. "
    #adding steps as points
    for step in step_list:
        step_point = {"type": "Feature","geometry":{"type":"Point","coordinates":[0,0]},"properties":{}}
        step_point["geometry"]["coordinates"][0] = step["start_location"]["lng"]
        step_point["geometry"]["coordinates"][1] = step["start_location"]["lat"]
        step_point["properties"]["html_instructions"] = step["html_instructions"]
        answer += step["html_instructions"]
        geoJson["features"].append(step_point)
    #last step point
    step_point = {"type": "Feature","geometry":{"type":"Point","coordinates":[0,0]},"properties":{}}
    step_point["geometry"]["coordinates"][0] = step_list[-1]["end_location"]["lng"]
    step_point["geometry"]["coordinates"][1] = step_list[-1]["end_location"]["lat"]
    step_point["properties"]["html_instructions"] = "You've reached your destination."
    geoJson["features"].append(step_point)
    answer += " You are there!"
    geoJson["answer"] = answer
    return geoJson


def routing(query):
    try:
        data = query["route"]
    except KeyError as e:
        print("Schema wrong, stopping.")
        sys.exit(1)
    try:
        # Extract start and end locations
        start = f"{data['startLocation']['name']} {data['startLocation']['address']}"
        end = f"{data['endLocation']['name']} {data['endLocation']['address']}"
        mode = data["transportationMode"] if "transportationMode" in data else "walking"

        # Geocode start and end points
        start_location = gmaps.geocode(start)[0]["geometry"]["location"]
        end_location = gmaps.geocode(end)[0]["geometry"]["location"]

        # Get route and travel time
        directions_result = gmaps.directions(
            origin=start_location,
            destination=end_location,
            mode=mode
        )
        
        directions_result = directions_result[0]
       
        geoJsonRoute = gmaps_routing_geojson(directions_result)

        if not directions_result:
            print("No route found.")
            return {}

        return geoJsonRoute

        # Extracting route details
        #travel_time = directions_result["legs"][0]["duration"]["text"]
        #distance = directions_result["legs"][0]["distance"]["text"]
        #steps = [
        #    step["html_instructions"]
        #    for step in directions_result["legs"][0]["steps"]
        #]

        ## Print results
        #print(f"Travel time: {travel_time}")
        #print(f"Distance: {distance}")
        #print("Route steps:")
        #for step in steps:
        #    print(f"- {step}")

        #return {
        #    "travel_time": travel_time,
        #    "distance": distance,
        #    "route_steps": steps,
        #}

    except KeyError as e:
        print(f"Error in query format: {e}")
        return {}



def do_query(query,name):
    task_list = get_tasks(query)
    for task in task_list:
        if task=="find_POI":
            result_geoJson = find_poi(query)
            with open('%s_%s.json'%(name,task), 'w') as f:
                json.dump(result_geoJson, f)
        elif task=="routing":
            result_geoJson = routing(query)
            with open('%s_%s.json'%(name,task), 'w') as f:
                json.dump(result_geoJson, f)
        else:
            print("Unknown task")

do_query(q1,"q1")  # True,False in uppercase please
do_query(q2,"q2")
do_query(q3,"q3")
do_query(q4,"q4")
do_query(q5,"q5")
#do_query(q6,"q6")  #doesn't work
#do_query(q7,"q7")  #transport mode transit, html error
do_query(q8,"q8")
do_query(q9,"q9")  #transport mode transit
do_query(q10,"q10")
#do_query(q11,"q11") #doesn't work, transport mode transit
do_query(q12,"q12") #transport mode transit
#do_query(q13,"q13") #will not work
do_query(q14,"q14") #nothing found (max price 80?)
do_query(q15,"q15")
do_query(q16,"q16") #nothing found
do_query(q17,"q17")
do_query(q18,"q18")
do_query(q19,"q19")  #nothing found
do_query(q20,"q20")  #nothing found
