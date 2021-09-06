from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types

# --- Menu ---
btnM = KeyboardButton('⬅️ Main menu')

Menu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnM)

# --- Main Menu ---
btnLang = KeyboardButton('🔎 Contacts 📞')
btnExch = KeyboardButton('💵 Exchange 💵')
btnRate = KeyboardButton('📊 Exchange rate 📊')
btnRez = KeyboardButton('🏛 Service reserves 🏛')
btnInfo = KeyboardButton('ℹ Information ℹ')

mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnLang, btnRez).add(btnExch, btnRate).add(btnInfo)

# --- Test inline ---
inline_btn_1 = InlineKeyboardButton('Первая кнопка!', callback_data='button1')

inlinemenu = InlineKeyboardMarkup(resize_keyboard = True).add(inline_btn_1)


# --- Language Menu ---
btnEN = KeyboardButton('English')
btnCN = KeyboardButton('中国人') #китайский юани
btnJP = KeyboardButton('日本語') #японский иены
btnRU = KeyboardButton('Русский')
btnESP = KeyboardButton('Española')
btnKR = KeyboardButton('한국어') #корейский воны
btnMain = KeyboardButton('⬅️ Main menu')

languMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnEN, btnCN, btnJP, btnRU, btnESP, btnKR, btnMain)

# --- Select currency ---
btnUSD = KeyboardButton('USD')
btnCNY = KeyboardButton('CNY') 
btnJPY = KeyboardButton('BTC')
btnRUB = KeyboardButton('RUB')
btnEUR = KeyboardButton('EUR')
btnKRW = KeyboardButton('KRW')
btnUAH = KeyboardButton('UAH')
btnBRL = KeyboardButton('BRL')
btnCAD = KeyboardButton('CAD')
btnMain = KeyboardButton('⬅️ Main menu')

currencyMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnUSD, btnCNY, btnJPY, btnRUB, btnEUR, btnKRW, btnBRL, btnUAH, btnCAD, btnMain)

# --- The next step ---
btnNext = KeyboardButton('The next step ➡️')
btnChosecurrency = KeyboardButton('⬅ Choose a currency')

nextMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnNext). add(btnChosecurrency)

# --- Continue ---
btnContinue = KeyboardButton('Continue ➡️')

ContinueMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnContinue)

# --- Final ---
btnFinal = KeyboardButton('I paid ✅')

FinalMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnFinal)

# --- Final ---
btnFinal = KeyboardButton('I paid ✅')
btnM = KeyboardButton('⬅️ Main menu')

FinM = ReplyKeyboardMarkup(resize_keyboard = True).add(btnFinal). add(btnM)
