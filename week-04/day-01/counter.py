# Create Counter class
# which has an integer field value
# when creating it should have a default value 0 or we can specify it when creating
# we can add(number) to this counter another whole number
# or we can add() without parameters just increasing the counter's value by one
# and we can get() the current value
# also we can reset() the value to the initial value
# Check if everything is working fine with the proper test
# Download test_counter.py and place it next to your solution
# Run the test file as a usual python program

class Counter(object):
    def __init__(self):
        self.integer_field = 0

    def add(self, number):
        self.integer_field += number
        return self.integer_field

    def get(self):
        return self.integer_field

    def reset(self):
        self.integer_field = 0
        return self.integer_field


integer1 = Counter()
integer1.add(16)

print(integer1.get())

integer1.reset()

print(integer1.get())