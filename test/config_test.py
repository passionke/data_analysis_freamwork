import unittest
from config import Config


class ConfigTest(unittest.TestCase):

    def test_config(self):
        cfg = Config()
        cfg.load("../feature_config.json")
        print(cfg.table)


if __name__ == '__main__':
    unittest.main()
