import sys

class Water():

    def __init__(self, list_of_commands):
        self.list_of_commands = list_of_commands
        self.total_cost = 0
        self.fixed_cost = 0
        self.fixed_capacity = 0
        self.variable_cost = 0
        self.variable_capacity = 0
        self.TWOBHK = 900
        self.THREEBHK = 1500
        self.CORPORATION_RATE = 1
        self.BOREWELL_RATE = 1.5
        self.TANKER_RATE = {
            '0-500': 2,
            '501-1500':3,
            '1501-3000': 5,
            '3000+': 8
        }

    def _fixed(self):
        if 'ALLOT_WATER' in list_of_commands[0]:
            list_of_allot_water_components = list_of_commands[0].split(" ")
            apartment_type = list_of_allot_water_components[-2]
            corporate_ratio = int(list_of_allot_water_components[-1].split(':')[0])
            borewell_ratio = int(list_of_allot_water_components[-1].split(':')[1])
            total_ratio = corporate_ratio + borewell_ratio
            fixed_capacity =  self._fixed_capacity(apartment_type)
            fixed_cost = self._fixed_cost(fixed_capacity, total_ratio, corporate_ratio, borewell_ratio)
            return fixed_capacity, fixed_cost

    def _fixed_capacity(self, apartment_type):
        return self.TWOBHK if apartment_type == '2' else self.THREEBHK

    def _fixed_cost(self, fixed_capacity, total_ratio, corporate_ratio, borewell_ratio):
        return round((fixed_capacity/total_ratio)*corporate_ratio*self.CORPORATION_RATE + (fixed_capacity/total_ratio)*borewell_ratio*self.BOREWELL_RATE)


    def _variable(self):
        number_of_guest = 0
        for command in list_of_commands:
            if 'ADD_GUESTS' in command:
                number_of_guest += int(command.split(" ")[-1])

        variable_capacity = self._variable_capacity(number_of_guest)
        variable_cost = self._variable_cost(variable_capacity)

        return variable_capacity, variable_cost

    def _variable_capacity(self, number_of_guest):
        return number_of_guest*300

    def _variable_cost(self,variable_capacity):
        if(variable_capacity < 501):
            return variable_capacity*self.TANKER_RATE['0-500']
        elif(variable_capacity > 500 and variable_capacity < 1501):
            return 500*self.TANKER_RATE['0-500'] + (variable_capacity - 500)*self.TANKER_RATE['501-1500']
        elif(variable_capacity > 1500 and variable_capacity < 3001):
            return 500*self.TANKER_RATE['0-500'] + 1000*self.TANKER_RATE['501-1500'] + (variable_capacity - 1500)*self.TANKER_RATE['1501-3000']
        else:
            return 500*self.TANKER_RATE['0-500'] + 1000*self.TANKER_RATE['501-1500'] + 1500*self.TANKER_RATE['1501-3000'] + (variable_capacity - 3000)*self.TANKER_RATE['3000+']

    def _calculate_cost(self):

        fixed_capacity, fixed_cost =  self._fixed() 
        variable_capacity, variable_cost = self._variable()
        total_capacity = fixed_capacity + variable_capacity
        total_cost = fixed_cost + variable_cost
        return total_capacity, total_cost

    def display(self):
        total_capacity, total_cost = self._calculate_cost()
        return total_capacity, total_cost
        


if __name__ == '__main__':

    #reading input file
    with open(sys.argv[1], 'r') as my_file:
        list_of_commands = my_file.read().split('\n')

    #output in cli
    water_cost = Water(list_of_commands)
    total_capacity, total_cost = water_cost.display()
    print(total_capacity, total_cost)



