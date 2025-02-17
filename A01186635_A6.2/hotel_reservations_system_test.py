"""
Module: hotel_reservation_system_test.py
This script implements test for all the hotel reservation system Objects and its methods
"""
import unittest
import os
from hote_reservations_system import Hotel, Customer, Reservation

class TestHotelReservationSystem(unittest.TestCase):
    """Test object for the Hotel Reservation Systems application"""
    @classmethod
    def setUpClass(cls):
        """Set up test environment before any test runs."""
        cls.test_hotel_file = "test_hotels.json"
        cls.test_customer_file = "test_customers.json"
        cls.test_reservation_file = "test_reservations.json"
        Hotel.DATA_FILE = cls.test_hotel_file
        Customer.DATA_FILE = cls.test_customer_file
        Reservation.DATA_FILE = cls.test_reservation_file

    def tearDown(self):
        """Clean up files after each test."""
        for file in [self.test_hotel_file, self.test_customer_file, self.test_reservation_file]:
            if os.path.exists(file):
                os.remove(file)

    def test_create_hotel(self):
        """Test hotel creation and persistence."""
        Hotel.create_hotel(1, "Test Hotel", "Test City", 10)
        hotels = Hotel.load_from_file()
        self.assertEqual(len(hotels), 1)
        self.assertEqual(hotels[0].name, "Test Hotel")

    def test_delete_hotel(self):
        """Test hotel deletion."""
        Hotel.create_hotel(2, "Delete Hotel", "Test City", 5)
        Hotel.delete_hotel(2)
        hotels = Hotel.load_from_file()
        self.assertEqual(len(hotels), 0)

    def test_create_customer(self):
        """Test customer creation and persistence."""
        Customer.create_customer(1, "Alice", "alice@example.com")
        customers = Customer.load_from_file()
        self.assertEqual(len(customers), 1)
        self.assertEqual(customers[0].name, "Alice")

    def test_create_reservation(self):
        """Test reservation creation and persistence."""
        Hotel.create_hotel(3, "Resort", "Beach City", 15)
        Customer.create_customer(3, "Charlie", "charlie@example.com")
        Reservation.create_reservation(1, 3, 3)
        reservations = Reservation.load_from_file()
        self.assertEqual(len(reservations), 1)
        self.assertEqual(reservations[0].customer_id, 3)
        self.assertEqual(reservations[0].hotel_id, 3)

    def test_display_hotels(self):
        """Test displaying hotel information (not raising errors)."""
        Hotel.create_hotel(4, "Display Hotel", "Display City", 20)
        try:
            Hotel.display_hotels()
            success = True
        except (FileNotFoundError, ValueError, KeyError) as error:
            print(f"Error encountered: {error}")
            success = False
        self.assertTrue(success)

if __name__ == '__main__':
    unittest.main()
