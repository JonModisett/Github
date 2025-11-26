from sklearn.linear_model import LinearRegression
import numpy as np

class Learner():
    def __init__(self, x, y):
        self.x = np.array(x).reshape(-1, 1)
        self.y = np.array(y)
    def testModel(self):
        #Create Model
        model = LinearRegression()

        #Learn from the data
        model.fit(self.x, self.y)
        x_test =float(input('X value to test with? '))
        x_test = np.array([[x_test]])
        y_pred = model.predict(x_test)

        # Print learned equation: y = mx + b
        slope = model.coef_[0].item()
        intercept = float(model.intercept_[0])

        # Output the prediction
        print(f"When x = {x_test[0][0]}, predicted y = {y_pred[0]}")
        print(f"Learned equation: y = {slope:.3f}x + {intercept:.3f}")


#Example
'''    
# Training data
# x: input (feature), y: output (label)
x = np.array([[1], [2], [3], [4], [5]])  # Shape: (5, 1)
y = np.array([3, 5, 7, 9, 11])           # Follows y = 2x + 1

# Test the model with new input
x_test = np.array([[6]])
y_pred = model.predict(x_test)

##Could Incorporate this to my model for out prompting of arrays##
def get_float_list(prompt):
    while True:
        raw = input(prompt)
        try:
            # split by commas and convert to floats
            float_list = [float(i.strip()) for i in raw.split(',')]
            return float_list
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")

def main():
    print("Enter your training data as comma-separated numbers.")
    x = get_float_list("Enter x values: ")
    y = get_float_list("Enter y values: ")

    if len(x) != len(y):
        print("Error: The number of x and y values must be the same.")
        return

    learner = Learner(x, y)
    learner.testModel()

if __name__ == "__main__":
    main()
'''

