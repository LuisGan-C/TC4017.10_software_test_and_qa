"""
Module: hotel_reservation_system.py
This script implements a hotel reservation system with three main abstractions:
- Hotel
- Reservation
- Customer
Data is stored in JSON files for persistence.
"""

import json
import os

class Hotel:
    """Represents a hotel with basic operations."""
    DATA_FILE = "hotels.json"

    def __init__(self, hotel_id, name, location, rooms_available):
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.rooms_available = rooms_available

    def to_dict(self):
        """Creates Hotel dict"""
        return self.__dict__

    @classmethod
    def save_to_file(cls, hotels):
        """Saves Data"""
        with open(cls.DATA_FILE, "w", encoding="utf-8") as file:
            json.dump([hotel.to_dict() for hotel in hotels], file, indent=4)

    @classmethod
    def load_from_file(cls):
        """Saves Data"""
        if not os.path.exists(cls.DATA_FILE):
            return []
        with open(cls.DATA_FILE, "r", encoding="utf-8") as file:
            return [cls(**data) for data in json.load(file)]

    @classmethod
    def create_hotel(cls, hotel_id, name, location, rooms_available):
        """Creates hotel"""
        hotels = cls.load_from_file()
        hotels.append(cls(hotel_id, name, location, rooms_available))
        cls.save_to_file(hotels)
        print(f"Hotel '{name}' created successfully.")

    @classmethod
    def delete_hotel(cls, hotel_id):
        """Deletes hotel"""
        hotels = [hotel for hotel in cls.load_from_file() if hotel.hotel_id != hotel_id]
        cls.save_to_file(hotels)
        print(f"Hotel ID {hotel_id} deleted.")

    @classmethod
    def display_hotels(cls):
        """Displays Hotels"""
        hotels = cls.load_from_file()
        for hotel in hotels:
            print(f"ID: {hotel.hotel_id}, Name: {hotel.name}")
            print(f"Location: {hotel.location}, Rooms: {hotel.rooms_available}")

class Customer:
    """Represents a customer."""
    DATA_FILE = "customers.json"

    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def to_dict(self):
        """Creates customer dict"""
        return self.__dict__

    @classmethod
    def save_to_file(cls, customers):
        """Saves to file"""
        with open(cls.DATA_FILE, "w", encoding="utf-8") as file:
            json.dump([customer.to_dict() for customer in customers], file, indent=4)

    @classmethod
    def load_from_file(cls):
        """Loads data"""
        if not os.path.exists(cls.DATA_FILE):
            return []
        with open(cls.DATA_FILE, "r", encoding="utf-8") as file:
            return [cls(**data) for data in json.load(file)]

    @classmethod
    def create_customer(cls, customer_id, name, email):
        """Creates customer"""
        customers = cls.load_from_file()
        customers.append(cls(customer_id, name, email))
        cls.save_to_file(customers)
        print(f"Customer '{name}' added.")

class Reservation:
    """Handles room reservations."""
    DATA_FILE = "reservations.json"

    def __init__(self, reservation_id, customer_id, hotel_id):
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id

    def to_dict(self):
        """Creates reservation dict"""
        return self.__dict__

    @classmethod
    def save_to_file(cls, reservations):
        """Saves data"""
        with open(cls.DATA_FILE, "w", encoding="utf-8") as file:
            json.dump([reservation.to_dict() for reservation in reservations], file, indent=4)

    @classmethod
    def load_from_file(cls):
        """Loads Data"""
        if not os.path.exists(cls.DATA_FILE):
            return []
        with open(cls.DATA_FILE, "r", encoding="utf-8") as file:
            return [cls(**data) for data in json.load(file)]

    @classmethod
    def create_reservation(cls, reservation_id, customer_id, hotel_id):
        """Creates Reservation"""
        reservations = cls.load_from_file()
        reservations.append(cls(reservation_id, customer_id, hotel_id))
        cls.save_to_file(reservations)
        print(f"Reservation ID {reservation_id} created successfully.")

if __name__ == "__main__":
    # Example usage
    Hotel.create_hotel(1, "Grand Hotel", "New York", 20)
    Customer.create_customer(1, "John Doe", "john@example.com")
    Reservation.create_reservation(1, 1, 1)
    Hotel.display_hotels()
