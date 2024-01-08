import stripe

from config import settings


stripe.api_key = settings.STRIPE_SECRET_KEY


class CreateSessionStripe:
    """
    Класс для создания объекта покупик и получения ссылки на этот объект
    """

    def __init__(self, name: str, description: str, currency: str, unit_amount: int, quantity: int):
        self.name = name
        self.description = description
        self.currency = currency
        self.unit_amount = unit_amount
        self.quantity = quantity

    def create_product(self) -> str:
        """
        Функция для создания продукта
        @return: возвращает id объекта
        """
        spc = stripe.Product.create(
            name=self.name,
            description=self.description)
        return spc['id']

    def create_price(self) -> str:
        """
        Функция для создания цены объекта
        @return: возвращает id цены объекта
        """
        spc = stripe.Price.create(
            currency=self.currency,
            unit_amount=self.unit_amount,
            product=self.create_product(),
        )
        return spc['id']

    def create_session(self) -> dict:
        """
        функция для создания сессии и получения словаря для дальнейшего использования
        @return: словарь значения созданной сессии
        """
        list_items = []
        items = {'price': self.create_price(), "quantity": self.quantity}
        list_items.append(items)
        scsc = stripe.checkout.Session.create(
            success_url="https://example.com/success",
            line_items=list_items,
            mode="payment",
        )
        return scsc
