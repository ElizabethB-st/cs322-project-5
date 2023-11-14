# UOCIS322 - Project 5 #
Brevet time calculator with MongoDB!


This project is based on RUSA's online calculator [https://rusa.org/octime_acp.html]. The algorithm is described here [https://rusa.org/pages/acp-brevet-control-times-calculator](https://rusa.org/pages/acp-brevet-control-times-calculator). 

The table below gives the minimum and maximum speeds for ACP brevets.

| Control Distance (km) | Min Speed (km/h) | Max Speed (km/h) |
|-----------------------|------------------|------------------|
| 0 - 200               | 15               | 34               |
| 200 - 400             | 15               | 32               |
| 400 - 600             | 15               | 30               |
| 600 - 1000            | 11.428           | 28               |
| 1000 - 1300           | 13.333           | 26               |

The calculation of a control's opening time is based on the maximum speed. Calculation of a control's closing time is based on the minimum speed.

## Distance, speed, and time calculation

When a distance in kilometers is divided by a speed in kilometers per hour, the result is a time measured in hours. For example, a distance of 100 km divided by a speed of 15 km per hour results in a time of 6.666666... hours. To convert that figure into hours and minutes, subtract the whole number of hours (6) and multiply the resulting fractional part by 60. The result is 6 hours, 40 minutes, expressed here as 6H40.

The calculator converts all inputs expressed in units of miles to kilometers and rounds (April 2021) truncates the result to the nearest kilometer before being used in calculations. Times are rounded to the nearest minute.

## Example 1:
Consider a 200km brevet with controls at 60km, 120km, 175km, and at the finish (205km).

Opening Times:

The controls at 60km, 120km, and 175km are each governed by a 34 km/hr maximum speed. 
60/34 = 1H46 
120/34 = 3H32 
175/34 = 5H09 
200/34 = 5H53

Note that we use a distance of 200km in the calculation, even though the route was slightly longer than that (205km).

Closing Times:

The minimum speed of 15 km/hr is used to determine the closing times. 
60/15 = 4H00 
120/15 = 8H00 
175/15 = 11H40

By the rules, the overall time limit for a 200km brevet is 13H30, even though by calculation, 200/15 = 13H20. The fact that the route is somewhat longer than 200km is irrelevant.

## Example 2:
Consider a 600km brevet with intermediate controls every 50km and an overall distance of 609km. A common question that we get is "which row of the minimum/maximum speed table do we use in this case: the 400-600 or the 600-1000"? This question illustrates a common misunderstanding of the algorithm. In fact, we use the speeds in each of the first three rows of the table: the first row of speeds for controls between 0 and 200km, the second row for controls between 200km and 400km, and the third row for controls between 400km and 600km.

Opening Times:

Consider the control at 100km. For that distance, the calculation is 100/34 = 2H56. For the control at 200km, we have 200/34 = 5H53.

For controls beyond the first 200km, the maximum speed decreases. Here the calculation is more difficult. Consider a control at 350km. We have 200/34 + 150/32 = 5H53 + 4H41 = 10H34. The 200/34 gives us the minimum time to complete the first 200km while the 150/32 gives us the minimum time to complete the next 150km. The sum gives us the control's opening time.

Similarly, a control at 550km is 200/34 + 200/32 + 150/30 = 17H08.

Closing Times:

Because the minimum speed for any distance in the first 600km is 15 km/hr, calculations can be done by dividing the control distance by 15. For example, a control at 550km is 550/15 = 36H40. The overall time limit is 600/15 = 40H00.

## Example 3:
Consider a control at 890km on a 1000km brevet.

Opening Time:

200/34 + 200/32 + 200/30 + 290/28 = 29H09

Closing Time:

600/15 + 290/11.428 = 65H23

## Oddities
By rule, the closing time for the starting point control (at 0km) is one hour after the official start. If the organizer places a control within the first 15km, that control will close before the starting point closes! For example, a control at 10km closes at 10/15 = 0H40. A control placed at 30km will close at 2H00, leaving just one hour to cover those 30 kilometers if the rider had left the start at its closing time. To prevent these situations, administrators should avoid placing controls too close to the start.

The algorithm used in France is somewhat different than the official standard described above. In the French variation, the maximum time limit for a control within the first 60km is based on 20 km/hr, plus 1 hour. Hence, the closing time of the starting point (0 km) is 0/20 + 1H00 = 1H00 as we expect. A control at 20 km would close at 20/20 + 1H00 = 2H00. A control at 60 km would close at 60/20 + 1H00 = 4H00 which is exactly what the standard rule would calculate (60/15 = 4H00). Beyond 60km, the standard algorithm applies. Note that the French variation solves the problem of placing controls early in the route. Alas, this algorithm is not permitted to be used for brevets outside France. (Update March 2018: It is now allowed to be used outside France.)

The table presented at the top of the page has a row for controls between 1000km and 1300km. Because the maximum length of an ACP brevet is 1000km, the last row of the table would never be used for an ACP brevet! Clearly, the table was intended to be used for 1200+km events sanctioned by the Randonneurs Mondiaux. However, Paris-Brest-Paris is not a Randonneurs Mondiaux sanctioned event, so it employs an entirely different calculator (see the discussion that accompanies the 1200+km calculator). Furthermore, the "1300" in the range should not be interpreted as an absolute rule. If you are using the calculator for an event well in excess of 1200km and you wish to use different minimum and maximum speed ranges, you should discuss your plans with the President of Randonneurs Mondiaux.

# Docker and Web app Intructions

Install Docker and Docker compose

Build the web flask app image using:

```
docker compose up
```
Launch http://hostname:5001 using your web browser

Input your desired Brevet information

You can save your information by clicking "Submit"

You can restore the saved information by clicking "Display"

# Authors

Author: Elizabeth Bowden

Contact: ebowden@uoregon.edu