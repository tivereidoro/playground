#!/usr/bin/python3

class Bike:
    def start():
        print('Start with kick')
    
class Scooter:
    def start():
        print('Start scooter with self')

class Car:
    def start():
        print('Start with key')


if __name__ == '__main__':
    bike1 = Bike()
    bike1.start()
    scooter1 = Scooter()
    scooter1.start()
    car = Car()
    car.start()