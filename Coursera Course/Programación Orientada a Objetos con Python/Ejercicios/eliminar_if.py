def calculate_local_cost_of(call):
    return call

def calculate_national_cost_of(call):
    return call

def calculate_international_cost_of(call):
    return call

def call_cost_calculate(call):
    cost = 0
    if call.is_local():
        cost = calculate_local_cost_of(call)
    elif call.is_national():
        cost = calculate_national_cost_of(call)
    elif call.is_international():
        cost = calculate_international_cost_of(call)
    return cost

#aplico polimorfismo para eliminar los if

class CallCostCalculator(object):

    def to_handle(self,klass,call):
        # Codigo que busca el CostCallCalculator correspondiente
        pass

    def calculate(self):
        raise NotImplementedError("Subclass Responsability")

class LocalCallCostCalculator(CallCostCalculator):
    def calculate(self):
        #Codigo de calculate_local_cost_of
        pass

class NationalCallCostCalculator(CallCostCalculator):
    def calculate(self):
        #Codigo de calculate_national_cost_of
        pass

class InternationalCallCostCalculator(CallCostCalculator):
    def calculate(self):
        #Codigo de calculate_international_cost_of
        pass

#cost_calculator = CallCostCalculator.to_handle(call)
#cost_calculator.calculate