def value_toothless():
    return 0
def value_sick(i):
    if i == 0:
        return 0
    return 4 + .9 * (3/4 * value_sick(i-1) + 1/4 * value_healthy(i-1))
def value_healthy(i):
    if i == 0:
        return 0
    return 10 + .9 * (3/4 * value_sick(i-1) + 1/4 * value_healthy(i-1))

# print('healthy', value_healthy(30))
# print('sick', value_sick(30))
    
candy = 7/8 * (10 + .9 * 51.1685) + 1/8 * (10 +.9*0)
vegetable = 3/4 * (4 + .9 * 51.1685) + 1/4 * (4 + .9 * 57.1685)

print("candy" , candy)
print("veg", vegetable)


candy = 3/4 * (10 + .9 * 51.1685) + 1/4 * (10 + .9 * 57.1685)
vegetable = 1 * (4 + .9 * 57.1685)

print("candy" , candy)
print("veg", vegetable)
