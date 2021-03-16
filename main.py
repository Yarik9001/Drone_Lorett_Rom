from os import system
import rospy
from clover import srv
from sensor_msgs.msg import Range
from std_srvs.srv import Trigger
import time

rospy.init_node('flight')

get_telemetry = rospy.ServiceProxy('get_telemetry', srv.GetTelemetry)
navigate = rospy.ServiceProxy('navigate', srv.Navigate)
navigate_global = rospy.ServiceProxy('navigate_global', srv.NavigateGlobal)
set_position = rospy.ServiceProxy('set_position', srv.SetPosition)
set_velocity = rospy.ServiceProxy('set_velocity', srv.SetVelocity)
set_attitude = rospy.ServiceProxy('set_attitude', srv.SetAttitude)
set_rates = rospy.ServiceProxy('set_rates', srv.SetRates)
land = rospy.ServiceProxy('land', Trigger)

timer = 0
stage = 0
x = 0.3
y = 0.4
color_flag = True
sket = 0


navigate(x=0, y=0, z=0.5, speed=0.1, frame_id='body', auto_arm=True)


while True:
    timer = time.clock()
    if stage == 0:
        x = 0.25
        y = 0.25
    if stage == 1:
        x = 1.25
        y = 1.25

    telemetry = get_telemetry(frame_id='aruco_map')
    navigate(x=x, y=y, z=0.5, speed=0.1, frame_id='aruco_map')
    if abs(x - telemetry.x) < 0.01 and abs(y - telemetry.y) < 0.01:
        stage += 1
        if stage == 2:
                stage = 0
                print(1)
    if sket == 5:
        break
    print(rospy.wait_for_message('rangefinder/range', Range))
    system('python3 sdrmin.py')


res = land()
if res.success:
    print('Copter is landing')
# arming(False)