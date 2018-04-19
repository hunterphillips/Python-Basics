# IMPORT another freaking python file
import functions
# use its 'methods'
print(functions.getSum(1, 2))

# Import specific method
from functions import sayHello
sayHello()
