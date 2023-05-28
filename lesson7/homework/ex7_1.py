from vectors import Vector #dlaczego samo 'import vectors' nie wystarczy?
def find_perpendicular(v1, v2):
    try:
        cross_vec = v1.cross(v2)
        cross_vec_len = cross_vec.length()
        unit_cross_vec_x = cross_vec.x / cross_vec_len
        unit_cross_vec_y = cross_vec.y / cross_vec_len
        unit_cross_vec_z = cross_vec.z / cross_vec_len
        unit_cross_vec = Vector(unit_cross_vec_x, unit_cross_vec_y, unit_cross_vec_z)
        return unit_cross_vec
    except AttributeError:
        print("parameters are not vectors!")
    except ZeroDivisionError:
        print("Vectors are parallel or zero lenght!") ##dlaczego jest none na końcu ??




w1 = Vector(2, 1, 4)
w2 = Vector(-1, 2, 3)
w3 = Vector(2, 1, 4)

t1 = (2, 1, 4)
t2 = (-1, 2, 3)





print(find_perpendicular(w1, w2))
print(find_perpendicular(w1, w3))
print(find_perpendicular(t1,t2))



