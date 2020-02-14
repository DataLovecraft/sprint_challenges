import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS

class AcmeProductTests(unittest.TestCase):

    def test_default_product_price(self):
        ''' Test default product price being 10 '''
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        ''' Test default product weight being 20 '''
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_product_flammability(self):
        ''' Test default product flammability being 0.5 '''
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)

    def test_default_stealability(self):
        ''' Test default stealability being 'Kinda stealable '''
        prod = Product('Test Product')
        steal = Product.stealability(prod)
        self.assertEqual(prod.stealability(), 'Kinda stealable')

    def test_default_explode(self):
        ''' Test default explode() being '...boom! '''
        prod = Product('Test Product')
        explode = Product.explode(prod)
        self.assertEqual(prod.explode(), '...boom!')



class AcmeReportTests(unittest.TestCase):

    def test_default_num_products(self):
        ''' Test length of product list being 30. '''
        products_len = len(generate_products())
        self.assertEqual(products_len, 30)

    def test_legal_names(self):
        """Check that all products have valid possible names."""
        for product in generate_products():
            adjective, noun = product.name.split()
            self.assertIn(adjective, ADJECTIVES)
            self.assertIn(noun, NOUNS)

if __name__ == '__main__':
    unittest.main()
