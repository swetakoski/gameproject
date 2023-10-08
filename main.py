import mysql.connector
from geopy import distance

connection = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='zombiator',
    user='root',
    password='Medowlarks04250.',
    autocommit=True
)

def get_dict_airportcoordinate_by_country():
    dict_airport_coordinate={}
    sql="SELECT country,latitude_deg, longitude_deg from airport"

    cursor=connection.cursor
    cursor.execute(sql)
    result=cursor.fetchall()
    if cursor.rowcount>0:
      for row in result:
          coordinate=(row[1], row[2])
          dict_airport_coordinate[row[0]]=coordinate
    return dict_airport_coordinate

def calculate_distance(current_location, country_name):
  my_db = connection.cursor()
  sql="SELECT country, latitude_deg, longitude_deg from airport WHERE country = %s"
  current_location=(current_location, )
  country_name=(country_name, )
  my_db.execute(sql, current_location)
  current_location_coordinate= my_db.fetchall()
  my_db.execute(sql, destination)
  country_name_coordinate= my_db.fetchall()
  return calculate_distance.calculate_distance((current_location_coordinate['latitude_deg'], current_location_coordinate['longitude_deg']),
          (country_name_coordinate['latitude_deg'], country_name_coordinate['longitude_deg'])).km


def get_dict_distance(current_location):
    dict_distance={}
    current_lat,current_lon=current_location
    airport_coordinates=get_dict_airportcoordinate_by_country()
    for country,coordinates in airport_coordinates.items():
        distance = calculate_distance()
        dict_distance[country] = distance
    return dict_distance

def command():
  if command == 1:
    country_name=input("Enter the name of the country you want to fly: ")
    distance=calculate_distance(current_location, country_name)
    need_fuel=fuel_consumed(distance)
    if user_fuel>=need_fuel:
        current_location=country_name
        user_fuel -=need_fuel
        if user_weapon>=need_weapon:
            user_weapon=need_weapon+reward
            user_money +=reward
        else:
          user_money=user_money/2