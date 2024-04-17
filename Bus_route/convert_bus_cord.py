import matsim

from helper_func import *
# Bus stop names
bus_stop_names = [
    "1A - Win-Win Boulevard Bus Station",
    "1A-Borey Lamazon Plaza",
    "1A-Kim Li Prek Phnov Over Fly",
    "1A-CP Cambodia Company",
    "1A-LSK Construction Material supply",
    "1A-Chea Sim Chomrouenroth High School",
    "1A-Beltie International School",
    "1A-PTT Gas Station",
    "1A-islam Church KM9",
    "1A-Hun Sen Chrang Chameh Primary School",
    "1A-Kilometer 7",
    "1A-Rusey Keo District Office",
    "1A-Borey New Wold",
    "1A-Samdach Oúv Health Cênter",
    "1A-TV stations CTN",
    "1A-Russey Keo High School",
    "1A-Intersection of Russey Keg Garden Line1A",
    "1A-baby care shop",
    "1A-Modern 5",
    "1A-Ponheakraek Primary school",
    "1A-Chaktomuk Health Center",
    "1A-Kolab School (Chroy Changva Bridge Base)",
    "1A-Calmet Hospital",
    "1A -Ministry of Information",
    "1A-National University of Managemet",
    "1A-BKC Intersection",
    "1A-Central Market Monivong Blvd",
    "1A-white hotel traffic light",
    "1A-koh pagoda",
    "1A-monivong road 214",
    "1A- preah yukunthor high school",
    "1A-monivong road 294",
    "1A-monivong road 360",
    "1A-monivong/mao tse tong",
    "1A-ministry of rural development",
    "1A-ministry of social affairs",
    "1A-royal university of law and economics",
    "1A-Boeung trabek high school",
    "1A- Intersection of monivong Flyover",
    "1A-Chbar Ampov Market",
    "1A-Caltex Gas Station",
    "1A-hun sen chbar Ampov high school",
    "1A-borey peng hout",
    "1A-chorrey hospital",
    "1A-Pannasastra international School Van Hong",
    "1A-Entrance to Borey veal Sbov",
    "1A-Preh Puthsatrian Pagoda",
    "1A-veal sbov pagoda"
]

coordinates = [
    (11.66571, 104.87608),
    (11.65355, 104.86145),
    (11.65421, 104.867),
    (11.6504, 104.86984),
    (11.6472, 104.87224),
    (11.64413, 104.87564),
    (11.64231, 104.87801),
    (11.63816, 104.88333),
    (11.6376, 104.88605),
    (11.63396, 104.89721),
    (11.63181, 104.90193),
    (11.62866, 104.9048),
    (11.6265, 104.90624),
    (11.61964, 104.91294),
    (11.61499, 104.91525),
    (11.61282, 104.9161),
    (11.6056, 104.91819),
    (11.60168, 104.91853),
    (11.59788, 104.91844),
    (11.59185, 104.91825),
    (11.58767, 104.91885),
    (11.58473, 104.91596),
    (11.58162, 104.91655),
    (11.57731, 104.91727),
    (11.57449, 104.91767),
    (11.57073, 104.91817),
    (11.56868, 104.91852),
    (11.56776, 104.91869),
    (11.56331, 104.91928),
    (11.56044, 104.91976),
    (11.55556, 104.92049),
    (11.55294, 104.9209),
    (11.54802, 104.92164),
    (11.54389, 104.92228),
    (11.53914, 104.92296),
    (11.5375, 104.9232),
    (11.53589, 104.92348),
    (11.53431, 104.92364),
    (11.53018, 104.9301),
    (11.53171, 104.93581),
    (11.5314, 104.93974),
    (11.53128, 104.94885),
    (11.53321, 104.9541),
    (11.53671, 104.95997),
    (11.5385, 104.96643),
    (11.53741, 104.96899),
    (11.536, 104.97221),
    (11.53389, 104.97718)
]



def tranform_cord():
    proccesed_cord = []

    transform = get_coordinate_transformation()
    for i in coordinates:
        proccesed_cord.append(convert_cord(i[1], i[0], transform))
    return proccesed_cord


cord_pros = tranform_cord()
print(cord_pros)

from lxml import etree

# Create the root element
transit_schedule = etree.Element("transitSchedule")

# Open a file in write mode
with open("transitSchedule_shell.xml", "w") as file:
    # Write the XML structure
    file.write('<transitSchedule>\n')
    file.write('\t<transitStops>\n')

    # Writing bus stop data
    for idx, (name, coord) in enumerate(zip(bus_stop_names, coordinates), start=1):
        file.write(
            f'\t\t<stopFacility id="{idx}" x="{cord_pros[idx-1][0]}" y="{cord_pros[idx-1][1]}" name="{name}" linkRefId="" isBlocking="true"/>\n')

    file.write('\t</transitStops>\n')

    file.write('</transitSchedule>\n')
