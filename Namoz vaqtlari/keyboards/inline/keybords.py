from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Toshkent', callback_data='tosh'),InlineKeyboardButton(text='Toshkent Viloyati', callback_data='tosh_vil')],
    [InlineKeyboardButton(text="Farg'ona", callback_data='far'),InlineKeyboardButton(text='Namangan', callback_data='nam')],
    [InlineKeyboardButton(text="Andijon", callback_data='and'),InlineKeyboardButton(text='Xorazm', callback_data='xor')],
    [InlineKeyboardButton(text='Jizzax', callback_data='jiz'),InlineKeyboardButton(text='Navoiy', callback_data='nav')],
    [InlineKeyboardButton(text='Samarqand', callback_data='samar'),InlineKeyboardButton(text='Sirdaryo', callback_data='sir')],
    [InlineKeyboardButton(text='Surxondaryo', callback_data='sur'),InlineKeyboardButton(text='Qashqadaryo', callback_data='qash')],
    [InlineKeyboardButton(text="Qoraqalpog'iston Respublikasi", callback_data='qoraqalpoq')],
])

menu1 = ReplyKeyboardMarkup(
    keyboard=[
    [KeyboardButton(text='Toshkent'), KeyboardButton(text='Toshkent Viloyati')],
    [KeyboardButton(text="Farg'ona"), KeyboardButton(text='Namangan')],
    [KeyboardButton(text="Andijon") ,KeyboardButton(text='Xorazm')],
    [KeyboardButton(text='Jizzax'), KeyboardButton(text='Navoiy')],
    [KeyboardButton(text='Samarqand'), KeyboardButton(text='Qarshi')],
    [KeyboardButton(text='Surxondaryo'), KeyboardButton(text='Qashqadaryo')],
    [KeyboardButton(text="Qoraqalpog'iston")],
])

choice = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Namoz vaqtlari', callback_data='namoztime')]
])

ortga = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Ortga🔙', callback_data='back')]
])

channel = InlineKeyboardMarkup(row_width= 1,inline_keyboard=[
    [InlineKeyboardButton(text='1-kanal', url='-1002127174067')],
    [InlineKeyboardButton(text="A'zo bo'ldim", callback_data="check")]
])