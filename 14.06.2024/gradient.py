# starting point
# learning rate alpha
# number of itrations

# example of gradiant descent

x=10
learning_rate = 0.01
num_iteration = 100

#create a loop for gradiant decent
for i in range (num_iteration):
    #compute our gradiant
    gradiant = 2 * x

    # update the x with new parameter that is new x

    x = x - learning_rate * gradiant
    print (f"iteration {i + 1}: x ={x}, f(x) = {x**2}")

print (f"minimum value of the  x:{x}")