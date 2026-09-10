class Product:
    def __init__(self, id=None, name = None,
                 Quantity=None, Price = None, coupon = None,VAT = None,cate_id = None):
        self.id = id
        self.name = name
        self.Quantity = Quantity
        self.Price = Price
        self.coupon = coupon
        self.VAT = VAT
        self.cate_id = cate_id
    def __str__(self):
        return (f"{self.id}\t{self.name}\t{self.Quantity}\t{self.Price}\t{self.coupon}\t{self.VAT}\t{self.cate_id}")
