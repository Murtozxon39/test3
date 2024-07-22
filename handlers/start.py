from aiogram import Router, F
from aiogram.types import Message, chat_member_updated
from aiogram.types.chat_member import ChatMember
from aiogram.filters import CommandStart, Command
from keyboards.start_menu import menu, menu2, menu3, menu4, menu5

start_router: Router = Router()


@start_router.message(CommandStart())
async def start_handler(msg: Message):
    await msg.answer (f"Assalomu alykum {msg.from_user.full_name} It-line dars botiga xush kelibsiz!", reply_markup=menu)


@start_router.message(F.text=="Darslarni boshlash")
async def dars_handler(msg: Message):
    await msg.answer("Quyidagi bo'limlardan birini tanlang.", reply_markup=menu2)


@start_router.message(F.text=="Dasturlash")
async def dasturlash(msg: Message):
    await msg.answer("Kursni tanlang: ", reply_markup=menu3)


@start_router.message(F.text=="Front-end")
async def front(msg: Message):
    await msg.answer("Kursni tanlang: ", reply_markup=menu4)


@start_router.message(F.text=="HTML")
async def html(msg: Message):
    await msg.answer("Dars sonini tanlang", reply_markup=menu5)
    # await msg.answer_video()

@start_router.message(F.text=="0-dars")
async def dars0 (msg: Message):
    await msg.answer_video('BAACAgIAAxkBAAOpZp4lLE7uIwP6EF9bsdBMS-IG_wkAAhYLAAJbWZlInNWoxY7DVi01BA', caption="HTML Darslari | 0-dars | Kurs haqida \n \n \n Youtube — https://www.youtube.com/@UlugbekSamigjonov \n \n \n Telegram — t.me/ulugbeksamigjonov")


@start_router.message(F.text=="1-dars")
async def dars1 (msg: Message):
    await msg.answer_video('BAACAgIAAxkBAAO3Zp4mAAHHpRmQ35bchPgV_y8S5VTEAAIXCwACW1mZSNLJ8Hjxm8zpNQQ', caption="HTML Darslari | 1-dars | Kurs haqida \n \n \n Youtube — https://www.youtube.com/@UlugbekSamigjonov \n \n \n Telegram — t.me/ulugbeksamigjonov")


@start_router.message(F.text=="2-dars")
async def dars1 (msg: Message):
    await msg.answer_video('BAACAgIAAxkBAAO5Zp4mEcQcA7fBVaJlSdL6TDqI2rYAAsoMAAJQv4FLohnOvna_wGw1BA', caption="HTML Darslari | 2-dars | Kurs haqida \n \n \n Youtube — https://www.youtube.com/@UlugbekSamigjonov \n \n \n Telegram — t.me/ulugbeksamigjonov")


@start_router.message(F.text=="3-dars")
async def dars1 (msg: Message):
    await msg.answer_video('BAACAgIAAxkBAAO7Zp4mGsNWf9ZosPCQ-BKi2gkylJgAAhoLAAJbWZlIYwO_H2Txq241BA', caption="HTML Darslari | 3-dars | Kurs haqida \n \n \n Youtube — https://www.youtube.com/@UlugbekSamigjonov \n \n \n Telegram — t.me/ulugbeksamigjonov")


@start_router.message(F.text=="4-dars")
async def dars1 (msg: Message):
    await msg.answer_video('BAACAgIAAxkBAAO9Zp4mISV6okFMIRZEwraE9LGdLNQAAhwLAAJbWZlI-d3w7-sn-5o1BA', caption="HTML Darslari | 4-dars | Kurs haqida \n \n \n Youtube — https://www.youtube.com/@UlugbekSamigjonov \n \n \n Telegram — t.me/ulugbeksamigjonov")


@start_router.message(F.text=="5-dars")
async def dars1 (msg: Message):
    await msg.answer_video('BAACAgIAAxkBAAO_Zp4mKos7_RFiyHPAC-1gM0aDN8UAAh0LAAJbWZlIT95m4Em7V8g1BA', caption="HTML Darslari | 5-dars | Kurs haqida \n \n \n Youtube — https://www.youtube.com/@UlugbekSamigjonov \n \n \n Telegram — t.me/ulugbeksamigjonov")


@start_router.message(F.text=="6-dars")
async def dars1 (msg: Message):
    await msg.answer_video('BAACAgIAAxkBAAPBZp4mMjhijET8Sbn-JSW2WtoufGQAAppJAALFeClJBJ_9L410UTc1BA', caption="HTML Darslari | 6-dars | Kurs haqida \n \n \n Youtube — https://www.youtube.com/@UlugbekSamigjonov \n \n \n Telegram — t.me/ulugbeksamigjonov")


@start_router.message(F.text=="7-dars")
async def dars1 (msg: Message):
    await msg.answer_video('BAACAgIAAxkBAAPDZp4mOYzTgeO1RgIWKaicnMqFBLIAAmEMAALYJaBLaIDRUO1QolE1BA', caption="HTML Darslari | 7-dars | Kurs haqida \n \n \n Youtube — https://www.youtube.com/@UlugbekSamigjonov \n \n \n Telegram — t.me/ulugbeksamigjonov")


@start_router.message(F.text=="8-dars")
async def dars1 (msg: Message):
    await msg.answer_video('BAACAgIAAxkBAAPFZp4mQT-WydZn6P-9A8_1yeTLRDwAAh8LAAJbWZlIMboPr6nNVRE1BA', caption="HTML Darslari | 8-dars | Kurs haqida \n \n \n Youtube — https://www.youtube.com/@UlugbekSamigjonov \n \n \n Telegram — t.me/ulugbeksamigjonov")


@start_router.message(F.text=="9-dars")
async def dars1 (msg: Message):
    await msg.answer_video('BAACAgIAAxkBAAPHZp4mUwjhjhO6iazwETpDtLDeyh0AAmIMAALYJaBLdKaljBCDcu01BA', caption="HTML Darslari | 9-dars | Kurs haqida \n \n \n Youtube — https://www.youtube.com/@UlugbekSamigjonov \n \n \n Telegram — t.me/ulugbeksamigjonov")


@start_router.message(F.text=="10-dars")
async def dars1 (msg: Message):
    await msg.answer_video('BAACAgIAAxkBAAPJZp4mXI0rQhhe2JOJCFqGt7dMNqsAAiALAAJbWZlI7zZJVLZncHg1BA', caption="HTML Darslari | 10-dars | Kurs haqida \n \n \n Youtube — https://www.youtube.com/@UlugbekSamigjonov \n \n \n Telegram — t.me/ulugbeksamigjonov")



