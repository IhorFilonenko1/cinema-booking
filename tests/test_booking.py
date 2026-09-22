import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import booking
import movies


class TestBooking(unittest.TestCase):
    def setUp(self):
        booking.bookings.clear()
        movies.get_movie(1)["seats"] = 60

    def test_book_tickets(self):
        result = booking.book_tickets(1, 2)
        self.assertIsNotNone(result)
        self.assertEqual(result["tickets"], 2)
        self.assertEqual(movies.get_movie(1)["seats"], 58)

    def test_book_tickets_no_seats(self):
        self.assertIsNone(booking.book_tickets(1, 999))

    def test_cancel_booking_restores_seats(self):
        result = booking.book_tickets(1, 3)
        booking.cancel_booking(result["id"])
        self.assertEqual(movies.get_movie(1)["seats"], 60)
        self.assertEqual(len(booking.get_bookings()), 0)

    def test_calculate_discount(self):
        self.assertEqual(booking.calculate_discount(200, 25), 150.0)
        self.assertEqual(booking.calculate_discount(200, 0), 200.0)


if __name__ == "__main__":
    unittest.main()
