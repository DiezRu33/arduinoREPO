
from robodk import *      # RoboDK API
from robolink import *    # Robot toolbox

RDK = robolink.Robolink()

robot = RDK.Item('%RoboDK items%')


pos_inicial = [0.000000, -90.000000, 85.150000, 0.000000, 0.000000, 0.000000]
pos_final = [-150.000000, -33.510000, 62.000000, 0.000000, -51.920000, -171.680000]
pos_added = [-50.000000, -113.510000, 62.000000, 0.000000, -71.920000, -111.680000]

# Program example:
item = RDK.Item('base')

if item.Valid():
    for i in range(0,3):
        robot.MoveJ(pos_inicial)
        robot.MoveJ(pos_final)   
    time.sleep(.8)     

    for i in range(0,5):
        robot.MoveJ(pos_added)
        time.sleep(.5)

print('Items in the station:')
itemlist = RDK.ItemList()
print(itemlist)
