import math

R, r, a = 8, 1, 4
TTx = -118.285492
TTy = 34.020517
t = 0.00

with open("spiro.kml", 'w') as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<kml xmlns="http://earth.google.com/kml/2.0">\n')
    f.write('<Document>\n')
    f.write('<Style id="z1">\n')
    f.write('<IconStyle><Icon><href>http://www.google.com/intl/en_us/mapfiles/ms/micons/blue-dot.png</href></Icon></IconStyle>\n')
    f.write('</Style>\n')
    f.write('<Placemark>\n')
    f.write('<styleUrl>#z1</styleUrl><Point><coordinates>-118.285492,34.020517</coordinates></Point>\n')
    f.write('</Placemark>\n')
    f.write('<Placemark>\n')
    f.write('<name>Spiro curve</name>\n')
    f.write('<Style><LineStyle><color>ff0000ff</color><width>2</width></LineStyle></Style>\n')
    f.write('<LineString>\n')
    f.write('<coordinates>\n')
    
    while t < 16 * math.pi:
        coord = ""
        x = (R + r) * math.cos((r / R) * t) - a * math.cos((1 + r / R) * t) 
        y = (R + r) * math.sin((r / R) * t) - a * math.sin((1 + r / R) * t) 
        new_x = x/10000 +TTx
        new_y = y/10000 +TTy
        coord = str(new_x)+ ',' +str(new_y) + '\n'
        f.write(coord)
        t += 0.01

    f.write('</coordinates>\n')
    f.write('</LineString>\n')
    f.write('</Placemark>\n')
    f.write('</Document></kml>\n')
