import discord
import random , requests , os
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            file_name = file.filename
            file_url = file.url
            await file.save(f'{file_name}')
            await ctx.send(f'file disimpan atas nama {file_name}')
            hasil = get_class('keras_model.h5', 'labels.txt' , file_name)

            if hasil[0] == 'kucing sphynx\n' and hasil[1] >= 0.6 :
                await ctx.send('INI ADALAH KUCING JENIS SPHYNX')
                await ctx.send('Ras kucing sphynx pertama kali muncul pada tahun 1960-an lalu di Kanada. Tak jarang, masyarakat sekitar menyebut kucing ini dengan nama kucing gundul. Kucing ras ini memiliki harga yang mahal, bahkan kucing sphynx dengan kualitas yang bagus mempunyai harga yang lebih mahal daripada sebuah motor baru, lho.')
                await ctx.send('untuk info lebih lengkap klik link berikut ini : https://www.gramedia.com/best-seller/kucing-tanpa-bulu/')

            elif hasil[0] == 'kucing persia\n' and hasil[1] >= 0.6 :
                await ctx.send('INI ADALAH KUCING JENIS PERSIA')
                await ctx.send('Kucing persia adalah ras kucing domestik berbulu panjang dengan karakter wajah bulat dan moncong pendek. Namanya mengacu pada Persia, nama lama Iran, di mana kucing serupa ditemukan. Sejak akhir abad 19, kucing jenis ini dikembangkan di Britania Raya dan Amerika Serikat usai Perang Dunia II.[1] Di Britania Raya, ras ini disebut kucing bulu panjang persia, dibagi dalam dua jenis, yaitu Chinchilla dengan warna perak cerah dan yang agak gelap.')
                await ctx.send('untuk info lebih lengkap klik link berikut ini : https://www.orami.co.id/magazine/kucing-persia?page=all')
            
            else :
                await ctx.send('GAMBAR BUKAN DIANTARA KUCING JENIS SPHYNX ATAU PERSIA')


    else:
        await ctx.send('ANDA TIDAK MENGIRIMKAN APAPUN')

bot.run("MTEzNDEwNTc3MjU4Mjc3Njg4Mg.GlSh0n.7eQWBSK9X7Mg-bnPY8_xWFwsJgXMP0oGAydDTM")