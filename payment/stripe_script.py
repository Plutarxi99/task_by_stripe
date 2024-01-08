import stripe

from payment.models import Order, Discount, Tax

from config import settings
from product.models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


def get_dc_value(discount_id):
    """
    Получение скидки на товары
    @param discount_id: объект скидки
    @return: процент скидки
    """
    discount = Discount.objects.get(pk=discount_id).discount
    return discount


def get_tx_value(tax_code_id):
    """
    Получение налога на товар
    @param tax_code_id: объект налога
    @return: процент налога
    """
    tax_code = Tax.objects.get(pk=tax_code_id).tax
    return tax_code


def get_list_item_buy(pk_order: int) -> list:
    """
    Получение списка товаров
    @param pk_order: объект списка товара
    @return: список продуктов
    """
    list_item_pk = Order.item.through.objects.values().filter(order_id=pk_order).values_list(
        'item_id', flat=True)
    list_item = Item.objects.filter(id__in=list(list_item_pk))
    return list_item


def create_product(name: str, description: str or None, tax_code=None) -> str:
    """
    Создание продукта
    @param name: название продукта
    @param description: описание продукта
    @param tax_code: налог
    @return: id созданного продукта
    """
    spc = stripe.Product.create(
        name=name,
        description=description,
        # tax_code=tax_code,
    )
    return spc['id']


def create_price(currency: str, unit_amount: int, product_id: str) -> str:
    """
    Создание цены на продукты
    @param currency: валюта оплаты
    @param unit_amount: цена на продукт
    @param product_id: объект созданного продукта
    @return: id созданной цены на продукт
    """
    spc = stripe.Price.create(
        currency=currency,
        unit_amount=unit_amount,
        product=product_id,
        # tax_behavior="exclusive",
    )
    return spc['id']


def get_list_items(id_price: str, quantity: int) -> dict:
    """
    Получение словаря для добавления в сессию
    @param id_price: id созданной цены на товар
    @param quantity: количество купленного товара
    @return: словарь id цены и количество товара
    """
    item_dict = {'price': id_price, "quantity": quantity}
    return item_dict


def get_discount(discount: int):
    """
    Получение скидки на товар
    @param discount: скидка на товар
    @return: словарь для добавлению в сессию
    """
    if discount:
        coupon = stripe.Coupon.create(
            percent_off=discount,
            duration="once",
        )
        return [{"coupon": coupon['id']}]
    return None


# def get_tax(tax):
#     tax = stripe.TaxRate.create(
#         display_name="VAT",
#         description="VAT Germany",
#         percentage=tax,
#         jurisdiction="RU",
#         inclusive=False,
#     )
#     return tax['id']


def create_session(list_items: list, coupon_id: str, tax_id=None) -> dict:
    """
    Создание сессии
    @param list_items: список продуктов
    @param coupon_id: id созданной скидки
    @param tax_id: id созданного налога
    @return: словарь созданной сессии
    """
    scsc = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=list_items,
        mode="payment",
        discounts=coupon_id,
    )
    return scsc


def validate_order(pk_order):
    order = Order.objects.filter(pk=pk_order)
    discount_id = tuple(order.values_list('discount', flat=True))[0]
    tax_code_id = tuple(order.values_list('tax', flat=True))[0]
    if discount_id and tax_code_id:
        discount = get_dc_value(discount_id)
        tax_code = get_tx_value(tax_code_id)
        return {'discount': discount, "tax_code": tax_code}
    elif discount_id is None:
        tax_code = get_tx_value(tax_code_id)
        return {'discount': None, "tax_code": tax_code}
    elif tax_code_id is None:
        discount = get_dc_value(discount_id)
        return {'discount': discount, "tax_code": None}
    else:
        return {'discount': None, "tax_code": None}
