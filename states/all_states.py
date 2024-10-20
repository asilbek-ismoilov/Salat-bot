from aiogram.fsm.state import State, StatesGroup

class Help(StatesGroup):
    help = State()

class SalatAdd(StatesGroup):
    name = State()
    img = State()
    description = State()