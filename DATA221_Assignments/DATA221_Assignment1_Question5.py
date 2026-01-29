# Circle Area Comparison with Validation

import math
def circleAreaCoverage(radiusOfCircle1, radiusOfCircle2):
    if type(radiusOfCircle1) != int or type(radiusOfCircle2) != int:
        return "Invalid input, both radii must be integers."
    if radiusOfCircle1 <= 0 or radiusOfCircle2 <= 0:
        return "Invalid input, both radii must be positive."
    area1 = math.pi * radiusOfCircle1 ** 2
    area2 = math.pi * radiusOfCircle2 ** 2
    if area1 >= area2:
        larger_circle = area1
        smaller_circle = area2
    else:
        larger_circle = area2
        smaller_circle = area1

    area_coverage_percentage = (smaller_circle / larger_circle) * 100
    return area_coverage_percentage

print(circleAreaCoverage(2, 6))
print(circleAreaCoverage(-2, 5))
print(circleAreaCoverage(2.5, 7))

