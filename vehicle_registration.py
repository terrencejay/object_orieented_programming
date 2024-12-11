class vehicle:
    def __init__(self, reg_num, type, owner):
        self.reg_num = reg_num
        self.type = type
        self.owner = owner
    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"{self.reg_num} updated to {new_owner}")
        
vehicle1 = vehicle("197NTU","Car","Terrence")
vehicle2 = vehicle("504JCD", "Bike", "Libby")

print(vehicle1.owner)
print(vehicle2.type)

vehicle1.update_owner("Terry")

print(vehicle1.owner)