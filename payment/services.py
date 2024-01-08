from payment.stripe_script import get_list_item_buy, validate_order, get_discount, create_product, create_price, \
    get_list_items, create_session


def get_session_for_order(pk_order):
    """
    Функция для создания ссылки для оплаты товара, также если оплата производиться нескольких товаров,
    то выбранный список товаров идёт в оплату этой сессии
    @param pk_order:
    @return:
    """
    list_items = []
    list_queryset = get_list_item_buy(pk_order)
    order = validate_order(pk_order)
    discount_order = order['discount']
    tax_code = order['tax_code']
    discount = get_discount(discount_order)
    # tax = get_tax(tax_code)
    for item in list_queryset:
        # product_id = create_product(name=item.name, description=item.description or None, tax_code=tax_code)
        product_id = create_product(name=item.name, description=item.description or None)
        id_price = create_price(currency=item.currency, unit_amount=item.price, product_id=product_id)
        # item_dict = get_list_items(id_price=id_price, quantity=item.quantity or 1)
        item_dict = get_list_items(id_price=id_price, quantity=1)
        list_items.append(item_dict)
    # return create_session(list_items, coupon_id=discount, tax_id=tax_code)
    return create_session(list_items, coupon_id=discount)
