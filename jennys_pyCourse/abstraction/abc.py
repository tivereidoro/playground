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
    bike = Bike()
    bike.start()
    scooter = Scooter()
    scooter.start()
    car = Car()
    car.start()