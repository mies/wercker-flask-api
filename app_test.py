from app import app

import unittest
import json

class StunticonTestCase(unittest.TestCase):

  def test_index(self):
    tester = app.test_client(self)
    response = tester.get('/stunticons.json', content_type='application/json')
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.data, json.dumps(["Motormaster", "Dead End", "Breakdown", "Wildrider", "Drag Strip"]))

if __name__ == '__main__':
    unittest.main()