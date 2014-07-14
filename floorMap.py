from flask import Flask, render_template, request, redirect, url_for
from BuildingClass import *

app = Flask(__name__)

# ------------Gloabal Vars--------------#
floors = ["Floor 1", "Floor 2", "Floor 3", "Floor 4", "Floor 5", "Floor 6", "Floor 7", "Floor 8"]
building_a = Building('a', 2)
building_b = Building('b', 5)
building_c = Building('c', 8)
#Need to move to more object oriented approach
#--------------------------------------#

#----------Page Response Functions-----#
@app.route('/')
def main():
    return render_template('index.html', floor_image='../static/img/nic.jpg', active='z')

@app.route('/mopac_a')
def mopac_a():
    building_a.activate()
    building_b.deactivate()
    building_c.deactivate()
    return reload()

@app.route('/mopac_b')
def mopac_b():
    building_a.deactivate()
    building_b.activate()
    building_c.deactivate()
    return reload()

@app.route('/mopac_c')
def mopac_c():
    building_a.deactivate()
    building_b.deactivate()
    building_c.activate()
    return reload()

@app.route("/floor/<int:floor_num>")
def floor(floor_num):
    if building_a.isActive:
        building_a.update_floor(floor_num)
    elif building_b.isActive:
        building_b.update_floor(floor_num)
    else:
        building_c.update_floor(floor_num)
    return reload()


#----------Page Response Functions----#

#----------Helper Function------------#
def reload():
    if building_a.isActive:
        return render_template('index.html',
                               floor_image='../static/img/nic' +building_a.building_id +str(building_a.current_floor())+ '.jpg'
                               , active_a='active', floors=floors[0:building_a.num_floors])
    elif building_b.isActive:
        return render_template('index.html',
                               floor_image='../static/img/nic' + building_b.building_id + str(building_b.current_floor()) + '.jpg',
                               active_b='active', floors=floors[0:building_b.num_floors])
    else:
        return render_template('index.html',
                               floor_image='../static/img/nic' + building_c.building_id + str(building_c.current_floor()) + '.jpg'
                               , active_c='active', floors=floors[0:building_c.num_floors])


if __name__ == '__main__':
    app.run(host='10.2.169.25')