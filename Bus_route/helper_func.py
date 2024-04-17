import pyproj
import math


def get_coordinate_transformation():
    """
    Get the coordinate transformation from WGS84 to UTM zone 48N (Phenom Peng).

    Returns:
    - transformer (pyproj.Transformer): Coordinate transformation object used in MatSim.
    """
    src_crs = "EPSG:4326"  # WGS84
    target_crs = "EPSG:32648"  # UTM zone 48N

    transformer = pyproj.Transformer.from_crs(src_crs, target_crs, always_xy=True)
    return transformer


def convert_cord(long, lat, transformer):
    """
    Apply coordinate transformation object on longitude and latitude coordinates.

    """
    #transformer = get_coordinate_transformation()

    # Perform the coordinate transformation
    utm_x, utm_y = transformer.transform(long, lat)
    return utm_x, utm_y


"""
# Example coordinates in WGS84 (latitude, longitude)
latitude = 11.5564
longitude = 104.9282

# Perform the coordinate transformation separately
utm_x = convert_cord(longitude, latitude)[0]
utm_y = convert_cord(longitude, latitude)[1]

print("UTM X-coordinate:", utm_x)
print("UTM Y-coordinate:", utm_y)
"""


def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points
    on the earth specified in decimal degrees.
    """
    # Convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    radius_of_earth = 6371  # Radius of Earth in kilometers
    distance = radius_of_earth * c

    return distance


def get_leg_mode(distance, duration_time):
    """
    Determine the mode of transportation based on the distance traveled and duration time.
    """

    # Calculate speed (in km/h)
    if duration_time == 0:
        return "walk"
    else:
        speed = distance / (duration_time / 3600)  # Convert duration time to hours

    if speed < 5:
        return "walk"  # Assume walking if speed is less than 5 km/h
    elif speed < 20:
        return "ride"  # Assume scooter if speed is less than 20 km/h
    else:
        return "car"  # Assume car if speed is greater than or equal to 20 km/h


def convert_time(start_time):
    # Format the end time as "HH:MM:SS"
    time_str = start_time.strftime("%H:%M:%S")
    start_hours, minutes, seconds = map(int, time_str.split(':'))

    # Calculate the total number of seconds since midnight
    start_time = start_hours * 3600 + minutes * 60 + seconds

    return start_time




def get_duration_time(start, end):
    duration = end - start
    return duration


def get_activity_type(hour):
    if 6 <= hour < 12:  # Morning
        return "work"
    elif 12 <= hour < 14:  # Lunchtime
        return "foodshop"
    elif 14 <= hour < 18:  # Afternoon
        return "work"
    else:  # Evening
        return "home"
