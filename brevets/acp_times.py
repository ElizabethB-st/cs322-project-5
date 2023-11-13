"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_acp.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow
import math


#  You MUST provide the following two functions
#  with these signatures. You must keep
#  these signatures even if you don't use all the
#  same arguments.

# create dictionarys for the specified time and location values
control_0_2 = {'start_dist': 0, 'end_dist': 200, 'min_speed': 15, 'max_speed': 34}
control_2_4 = {'start_dist': 200, 'end_dist': 400, 'min_speed': 15, 'max_speed': 32}
control_4_6 = {'start_dist': 400, 'end_dist': 600, 'min_speed': 15, 'max_speed': 30}
control_6_10 = {'start_dist': 600, 'end_dist': 1000, 'min_speed': 11.428, 'max_speed': 28}


def control_st_calc(control, max_speed):
   raw_time = control / max_speed
   hour = math.floor(raw_time)
   frac_minutes = raw_time - hour
   minute = round(frac_minutes * 60)
   return_val = {'hour': hour, 'minute': minute}
   return return_val

def control_cl_calc(control, min_speed):
   raw_time = control / min_speed
   hour = math.floor(raw_time)
   frac_minutes = raw_time - hour
   minute = round(frac_minutes * 60)
   return_val = {'hour': hour, 'minute': minute}
   return return_val

def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
   """
   Args:
      control_dist_km:  number, control distance in kilometers
      brevet_dist_km: number, nominal distance of the brevet
         in kilometers, which must be one of 200, 300, 400, 600,
         or 1000 (the only official ACP brevet distances)
      brevet_start_time:  An arrow object
   Returns:
      An arrow object indicating the control open time.
      This will be in the same time zone as the brevet start time.
   """
   time = arrow.get(brevet_start_time)
   hour = 0
   minute = 0

   #if the control is longer than the brevet the calulation should be with brevet instead
   if control_dist_km > brevet_dist_km:
      control = brevet_dist_km
   else:
      control = control_dist_km
      
   if control <= 200:
      time_result = control_st_calc(control, control_0_2['max_speed'])
      hour = time_result['hour']
      minute = time_result['minute']
   elif control <= 400:
      #calcalute when distance is <=200
      time_result_1 = control_st_calc(200, control_0_2['max_speed'])
   
      #calculate when distance is >200
      remain_control_dist = control - 200
      time_result_2 = control_st_calc(remain_control_dist, control_2_4['max_speed'])

      hour = time_result_1['hour'] + time_result_2['hour']
      minute = time_result_1['minute'] + time_result_2['minute']
   elif control <= 600:
      #calcalute when distance is <=200
      time_result_1 = control_st_calc(200, control_0_2['max_speed'])

      #calculate when distance is <=400
      time_result_2 = control_st_calc(200, control_2_4['max_speed'])

      #calulate remaining distance with new start time
      remain_control_dist = control - 400
      time_result_3 = control_st_calc(remain_control_dist, control_4_6['max_speed'])
      
      hour = time_result_1['hour'] + time_result_2['hour'] + time_result_3['hour']
      minute = time_result_1['minute'] + time_result_2['minute'] + time_result_3['minute']
   elif control <= 1000:
      #calcalute when distance is <=200
      time_result_1 = control_st_calc(200, control_0_2['max_speed'])

      #calculate when distance is <=400
      time_result_2 = control_st_calc(200, control_2_4['max_speed'])

      #calulate when distance is <=600
      time_result_3 = control_st_calc(200, control_4_6['max_speed'])
      
      #calulate remaing distance
      remain_control_dist = control - 600
      time_result_4 = control_st_calc(remain_control_dist, control_6_10['max_speed'])
      hour = time_result_1['hour'] + time_result_2['hour'] + time_result_3['hour'] + time_result_4['hour']
      minute = time_result_1['minute'] + time_result_2['minute'] + time_result_3['minute'] + time_result_4['minute']

   start_time = time.shift(hours=hour, minutes=minute)
   return start_time


def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
   """
   Args:
      control_dist_km:  number, control distance in kilometers
         brevet_dist_km: number, nominal distance of the brevet
         in kilometers, which must be one of 200, 300, 400, 600, or 1000
         (the only official ACP brevet distances)
      brevet_start_time:  An arrow object
   Returns:
      An arrow object indicating the control close time.
      This will be in the same time zone as the brevet start time.
   """
   time = arrow.get(brevet_start_time)
   hour = 0
   minute = 0

   #if the control is longer than the brevet the calulation should be with brevet instead
   if control_dist_km > brevet_dist_km:
      control = brevet_dist_km
   else:
      control = control_dist_km

   #if the control is 0 close time should be 1hr
   if control == 0:
      hour = 1
   elif control <= 60:
      time_result = control_st_calc(control, 20)
      hour = time_result['hour'] + 1
      minute = time_result['minute']
   elif control == 200 and brevet_dist_km == 200:
      hour = 13
      minute = 30
   elif control <= 600:
      time_result = control_st_calc(control, control_0_2['min_speed'])
      hour = time_result['hour']
      minute = time_result['minute']
   elif control <= 1000:
      #calcalute when distance is <=600
      time_result_1 = control_st_calc(600, control_4_6['min_speed'])
      #calulate remaining distance with new start time
      remain_control_dist = control - 600
      time_result_2 = control_st_calc(remain_control_dist, control_6_10['min_speed'])
      hour = time_result_1['hour'] + time_result_2['hour']
      minute = time_result_1['minute'] + time_result_2['minute']

   close_time = time.shift(hours=hour, minutes=minute)
   return close_time
