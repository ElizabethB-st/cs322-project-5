"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""

import nose    # Testing framework
import logging
import arrow
import acp_times
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

#example #1 from https://rusa.org/pages/acp-brevet-control-times-calculator

def test_ex1_open():
    brevet_dist_km = 200
    brevet_start_time = arrow.now()
    control_1_km = 60
    control_2_km = 120
    control_3_km = 175
    control_4_km = 205

    open_time_1 = acp_times.open_time(control_1_km, brevet_dist_km, brevet_start_time)
    open_time_2 = acp_times.open_time(control_2_km, brevet_dist_km, brevet_start_time)
    print(open_time_2)
    open_time_3 = acp_times.open_time(control_3_km, brevet_dist_km, brevet_start_time)
    open_time_4 = acp_times.open_time(control_4_km, brevet_dist_km, brevet_start_time)

    assert open_time_1 == brevet_start_time.shift(hours=1, minutes=46)
    assert open_time_2 == brevet_start_time.shift(hours=3, minutes=32)
    assert open_time_3 == brevet_start_time.shift(hours=5, minutes=9)
    assert open_time_4 == brevet_start_time.shift(hours=5, minutes=53)


def test_ex1_close():
    brevet_dist_km = 200
    brevet_start_time = arrow.now()
    control_1_km = 60
    control_2_km = 120
    control_3_km = 175
    control_4_km = 205

    close_time_1 = acp_times.close_time(control_1_km, brevet_dist_km, brevet_start_time)
    close_time_2 = acp_times.close_time(control_2_km, brevet_dist_km, brevet_start_time)
    close_time_3 = acp_times.close_time(control_3_km, brevet_dist_km, brevet_start_time)
    close_time_4 = acp_times.close_time(control_4_km, brevet_dist_km, brevet_start_time)

    assert close_time_1 == brevet_start_time.shift(hours=4, minutes=0)
    assert close_time_2 == brevet_start_time.shift(hours=8, minutes=0)
    assert close_time_3 == brevet_start_time.shift(hours=11, minutes=40)
    assert close_time_4 == brevet_start_time.shift(hours=13, minutes=30)

#example #2 from https://rusa.org/pages/acp-brevet-control-times-calculator
def test_ex2_open():
    brevet_dist_km = 600
    brevet_start_time = arrow.now()
    control_1_km = 100
    control_2_km = 200
    control_3_km = 350
    control_4_km = 550

    open_time_1 = acp_times.open_time(control_1_km, brevet_dist_km, brevet_start_time)
    open_time_2 = acp_times.open_time(control_2_km, brevet_dist_km, brevet_start_time)
    open_time_3 = acp_times.open_time(control_3_km, brevet_dist_km, brevet_start_time)
    open_time_4 = acp_times.open_time(control_4_km, brevet_dist_km, brevet_start_time)

    assert open_time_1 == brevet_start_time.shift(hours=2, minutes=56)
    assert open_time_2 == brevet_start_time.shift(hours=5, minutes=53)
    assert open_time_3 == brevet_start_time.shift(hours=10, minutes=34)
    assert open_time_4 == brevet_start_time.shift(hours=17, minutes=8)

def test_ex2_close():

    brevet_dist_km = 600
    brevet_start_time = arrow.now()
    control_2_km = 200
    control_4_km = 550
    control_5_km = 609

    close_time_2 = acp_times.close_time(control_2_km, brevet_dist_km, brevet_start_time)
    close_time_4 = acp_times.close_time(control_4_km, brevet_dist_km, brevet_start_time)
    close_time_5 = acp_times.close_time(control_5_km, brevet_dist_km, brevet_start_time)

    assert close_time_2 == brevet_start_time.shift(hours=13, minutes=20)
    assert close_time_4 == brevet_start_time.shift(hours=36, minutes=40)
    assert close_time_5 == brevet_start_time.shift(hours=40, minutes=0)

#example #3 from https://rusa.org/pages/acp-brevet-control-times-calculator
def test_ex3_open():
    brevet_dist_km = 1000
    brevet_start_time = arrow.now()
    control_1_km = 890

    open_time_1 = acp_times.open_time(control_1_km, brevet_dist_km, brevet_start_time)

    assert open_time_1 == brevet_start_time.shift(hours=29, minutes=9)

def test_ex3_close():
    brevet_dist_km = 1000
    brevet_start_time = arrow.now()
    control_1_km = 890

    close_time_1 = acp_times.close_time(control_1_km, brevet_dist_km, brevet_start_time)

    assert close_time_1 == brevet_start_time.shift(hours=65, minutes=23)

#oddities from https://rusa.org/pages/acp-brevet-control-times-calculator
def test_odd_close():
    brevet_dist_km = 200
    brevet_start_time = arrow.now()
    control_1_km = 0
    control_2_km = 10
    control_3_km = 20
    control_4_km = 30
    control_5_km = 60 

    close_time_1 = acp_times.close_time(control_1_km, brevet_dist_km, brevet_start_time)
    close_time_2 = acp_times.close_time(control_2_km, brevet_dist_km, brevet_start_time)
    close_time_3 = acp_times.close_time(control_3_km, brevet_dist_km, brevet_start_time)
    close_time_4 = acp_times.close_time(control_4_km, brevet_dist_km, brevet_start_time)
    close_time_5 = acp_times.close_time(control_5_km, brevet_dist_km, brevet_start_time)

    assert close_time_1 == brevet_start_time.shift(hours=1, minutes=0)
    assert close_time_2 == brevet_start_time.shift(hours=1, minutes=30)
    assert close_time_3 == brevet_start_time.shift(hours=2, minutes=0)
    assert close_time_4 == brevet_start_time.shift(hours=2, minutes=30)
    assert close_time_5 == brevet_start_time.shift(hours=4, minutes=0)