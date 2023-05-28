import math

points = [(-1,-0.25),(-0.2,0.2),(0,0),(0,0.3),(0.25,0.3),(1,1),(1.5,1.5)]



print("list of points in unit circle: ",
      list(filter((lambda x: math.sqrt(abs(x[0])) + math.sqrt(abs(x[1])) <1),  points)))
print("list of points with positive coordinates: ",
      list(filter((lambda x: x[0]>0 and x[1]>0),  points)))

points.sort(key=lambda p: (-p[1],p[0]))
print("points with decreasing y and increasing x: ", points)

points.sort(key=lambda p: (abs(p[0]) + abs(p[1])))
print("points with increasing abs(x)+abs(y): ",points)



