from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart, Command
from loader import router, bot
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from keyboards.defoult.keybords import *
from keyboards.inline.keybords import *
from request import namoz


@router.message(CommandStart())
async def start(msg: Message):
    await msg.answer(f"Assalomu aleykum {msg.from_user.full_name}!😊")
    await check_subscription(msg)

async def check_subscription(message):
    channel_id = "Your_Group_ID"  # Kanal IDsi
    user_id = message.from_user.id
    try:
        member = await bot.get_chat_member(chat_id=channel_id, user_id=user_id)
        if member.status != 'left':
            await message.answer("Shahringizni tanlang:👇🏻", reply_markup=menu)
        else:
            await message.answer(
                "Assalomu alaykum! Kanallarga obuna bo'lishingizni so'raymiz.\nA'zo bo'lganingizdan so'ng /start buyrug'ini yuboring",
                reply_markup=InlineKeyboardMarkup(
                    inline_keyboard=[[InlineKeyboardButton(text="A'zo bo'lish", url="Your_Group_Link")]]
                )
            )
    except Exception as e:
        print("Xatolik sodir bo'ldi:", e)
        await message.answer("Uzr, qandaydir xatolik yuz berdi. Iltimos, keyinroq urinib ko'ring.")

city_callback_map = {
    'tosh': 'Toshkent',
    'tosh_vil': 'Angren',
    'far': "Farg'ona",
    'nam': 'Namangan',
    'and': 'Andijon',
    'xor': 'Xiva',
    'jiz': 'Jizzax',
    'nav': 'Navoiy',
    'samar': 'Samarqand',
    'sir': 'Guliston',
    'sur': 'Termiz',
    'qash': 'Qarshi',
    'qoraqalpoq': 'Nukus',
}

@router.callback_query(F.data.in_(city_callback_map.keys()))
async def weath(call: CallbackQuery):
    city = city_callback_map[call.data]
    response_message = namoz(city)
    await call.message.delete()
    await call.message.answer(response_message, reply_markup=ortga)

@router.callback_query(F.data == 'back')
async def back1(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Shahringiz ob-havosini tanlang:👇🏻", reply_markup=menu)

@router.message(Command('id'))
async def nothing(msg: Message):
    await msg.answer(f"Gr ID si: {msg.chat.id}")
