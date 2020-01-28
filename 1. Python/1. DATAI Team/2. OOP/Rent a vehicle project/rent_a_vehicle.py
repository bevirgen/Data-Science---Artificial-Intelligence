# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 23:26:13 2020

@author: berka
"""

import datetime

# parent class
class RentVehicle:
    
    def __init__(self,count):
        self.count = count
        self.now = 0
    
    def displayCount(self):
        print('{} vehicle available for rent'.format(self.count))
        return self.count
    
    def rentHourly(self, n):
        if n <= 0:
            print('Invalid number, number is should be positive')
            return None
        elif n > self.count:
            print('You can rent {} vehicle '.format(self.count))
            return None
        else:
            self.now = datetime.datetime.now().hour
            print("Rented {} vehicle for hourly at {} o'clock".format(n,self.now))
            self.count -= n
            return self.now
    
    def rentDaily(self, n):
        if n <= 0:
            print('Invalid number, number is should be positive')
            return None
        elif n > self.count:
            print('You can rent {} vehicle '.format(self.count))
            return None
        else:
            self.now = datetime.datetime.now().hour
            print("Rented {} vehicle for daily at {} o'clock".format(n,self.now))
            self.count -= n
            return self.now
    
    def returnVehicle(self, request, brand):
        car_h_price = 8
        car_d_price = car_h_price * 0.85 * 24
        bike_h_price = 3
        bike_d_price = bike_h_price * 0.75 * 24
        
        rentalTime, rentalBasis, numberOfVehicle = request
        bill = 0
        
        if brand == 'car':
            if rentalTime and rentalBasis and numberOfVehicle:
                self.count += numberOfVehicle
                now = datetime.datetime.now().hour
                rentalPeriod = abs(rentalTime - now)
                
                if rentalBasis == 1: #  hourly
                    bill = rentalPeriod * car_h_price * numberOfVehicle
                    
                elif rentalBasis == 2: #  daily
                    bill = rentalPeriod * car_d_price * numberOfVehicle
                    
                if (2 <= numberOfVehicle):
                    print('You earned %20 discount')
                    bill *= 0.8
                    
                print('Thanks for choosing us.\nThe fee you have to pay: {} TRY'.format(bill))
                return bill
        
        elif brand == 'bike':
            if rentalTime and rentalBasis and numberOfVehicle:
                self.count += numberOfVehicle
                now = datetime.datetime.now().hour
                rentalPeriod = abs(rentalTime - now)
                
                if rentalBasis == 1: #  hourly
                    bill = rentalPeriod * bike_h_price * numberOfVehicle
                    
                elif rentalBasis == 2: #  daily
                    bill = rentalPeriod * bike_d_price * numberOfVehicle
                    
                if (5 <= numberOfVehicle):
                    print('You earned %20 discount')
                    bill *= 0.75
                    
                print('Thanks for choosing us.\nThe fee you have to pay: {} TRY'.format(bill))
                return bill
        else:
            print('You did not rent any vehicle' )
    
# child class (car)
class CarRent(RentVehicle):
    
    global discount_rate
    discount_rate = 0.2
    
    def __init__(self, count):
        super().__init__(count)
    
    def discount(self, b):
        bill = b - b*discount_rate
        return bill

# child class (bike)    
class BikeRent(RentVehicle):
    
    def __init__(self, count):
        super().__init__(count)

# customer
class Customer():
    
    def __init__():
        pass
    
    def requestVehicle():
        pass
    
    def returnVehicle():
        pass