class Converter:
    def distance(dist, unit, point_unit):
        if point_unit == 'km':
            if unit == 'mi':
                return dist * 1.60934
            if unit == 'km':
                return dist
        elif point_unit == 'mi':
            if unit == 'km':
                return dist * 0.621371
            if unit == 'mi':
                return dist
        elif point_unit == 'm':
            if unit == 'km':
                return dist * 1000
            if unit == 'mi':
                return dist * 1609.34
            if unit == 'm':
                return dist
            if unit == 'ft':
                return dist * 0.3048
        elif point_unit == 'ft':
            if unit == 'm':
                return dist * 3.28084
            if unit == 'km':
                return dist * 3280.84
            if unit == 'mi':
                return dist * 5280
            if unit == 'ft':
                return dist
    
    def temperature(temp, unit, point_unit):
        if point_unit == 'C':
            if unit == 'F':
                return (temp - 32) * 5 / 9
            if unit == 'K':
                return temp - 273.15
            if unit == 'C':
                return temp
        elif point_unit == 'F':
            if unit == 'C':
                return temp * 9 / 5 + 32
            if unit == 'K':
                return (temp - 273.15) * 9 / 5 + 32
            if unit == 'F':
                return temp
        elif point_unit == 'K':
            if unit == 'C':
                return temp + 273.15
            if unit == 'F':
                return (temp - 32) * 5 / 9 + 273.15
            if unit == 'K':
                return temp
    
    def weight(mass, unit, point_unit):
        if point_unit == 'kg':
            if unit == 'lb':
                return mass * 0.453592
            if unit == 'g':
                return mass * 0.001
            if unit == 'oz':
                return mass * 0.0283495
            if unit == 'kg':
                return mass
        elif point_unit == 'lb':
            if unit == 'kg':
                return mass * 2.20462
            if unit == 'g':
                return mass * 0.00220462
            if unit == 'oz':
                return mass * 0.0625
            if unit == 'lb':
                return mass
        elif point_unit == 'g':
            if unit == 'kg':
                return mass * 1000
            if unit == 'lb':
                return mass * 453.592
            if unit == 'oz':
                return mass * 28.3495
            if unit == 'g':
                return mass
        elif point_unit == 'oz':
            if unit == 'kg':
                return mass * 35.274
            if unit == 'lb':
                return mass * 16
            if unit == 'g':
                return mass * 0.035274
            if unit == 'oz':
                return mass
