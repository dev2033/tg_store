from aiogram.dispatcher.filters.state import StatesGroup, State


class ProductState(StatesGroup):
    """Стейт для добавления товара"""
    title = State()
    body = State()
    image = State()
    price = State()
    confirm = State()


class CategoryState(StatesGroup):
    """Стейт для категории"""
    title = State()
