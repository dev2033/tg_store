from aiogram.dispatcher.filters.state import StatesGroup, State


class CheckoutState(StatesGroup):
    """Стейт для оформления заказа"""
    check_cart = State()
    name = State()
    address = State()
    confirm = State()
