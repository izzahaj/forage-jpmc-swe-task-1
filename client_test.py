import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      stock = quote['stock']
      top_bid = quote['top_bid']['price']
      top_ask = quote['top_ask']['price']
      expected_price = (top_bid + top_ask) / 2
      self.assertEqual(getDataPoint(quote), (stock, top_bid, top_ask, expected_price))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      stock = quote['stock']
      top_bid = quote['top_bid']['price']
      top_ask = quote['top_ask']['price']
      expected_price = (top_bid + top_ask) / 2
      self.assertEqual(getDataPoint(quote), (stock, top_bid, top_ask, expected_price))

  """ ------------ Add more unit tests ------------ """
  def test_getDataPoint_invalidPrices(self):
    quotes = [
      {'top_ask': {'price': None, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': None, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': None, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': None, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    for quote in quotes:
      with self.assertRaises(TypeError):
        getDataPoint(quote)

  def test_getRatio_validPrices(self):
    price_a = 120.48
    price_b = 117.87
    expected_ratio = price_a / price_b
    self.assertEqual(getRatio(price_a, price_b), expected_ratio)
    
  def test_getRatio_zeroDivision(self):
    price_a = 120.48
    price_b = 0
    self.assertIsNone(getRatio(price_a, price_b))

  def test_getRation_negativePrices(self):
    price_a = -120.48
    price_b = 117.87
    expected_ratio = price_a / price_b
    self.assertEqual(getRatio(price_a, price_b), expected_ratio)


if __name__ == '__main__':
    unittest.main()
