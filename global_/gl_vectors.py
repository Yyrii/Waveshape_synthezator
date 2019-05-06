from global_.setup import*

# vector parts
vector_y = []
vector_y.append(default_val) # later functions

lines = []
#   lines is vector, helping create id of each line, in equiwalent position
for i in range(width):   # u cannot exceed the window, those samples will not be taken into consideration
    lines.append(0)