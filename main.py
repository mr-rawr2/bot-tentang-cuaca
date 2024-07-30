import discord
from discord.ext import commands
import json
import requests


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def halo(ctx):
    await ctx.send(f'Hi! aku bot {bot.user}! ada yang ku bisa bantu?')

@bot.command()
async def informasi_iklim(ctx):
    await ctx.send(f'silahkan memilih iklim apa yang ingin anda ketahui(jangan pakai tanda dolar):')
    await ctx.send(f'\n-iklim tropis \n-iklim subtropis \n-iklim sedang \n-iklim dingin \n-iklim fisis')
    message2 = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    message2 = str(message2.content)

    if message2 == 'iklim tropis':
        await ctx.send('Iklim tropis terjadi di kawasan sekitar ekuator atau garis khatulistiwa seperti Indonesia. Pada iklim tropis, cuaca hangat sepanjang hari dan tidak ada musim dingin. Sebagian iklim tropis merupakan hutan hujan tropis di kawasan-kawasan pada garis khatulistiwa. Sementara agak jauh dari garis khatulistiwa, daerahnya agak kering hingga padang pasir.')
    elif message2 == 'iklim subtropis':
        await ctx.send('Jenis iklim subtropis ada di daerah dengan lintang 20 hingga 40 derajat. Daerah dengan iklim subtropis punya suhu harian dan musiman yang lebih beragam dari daerah tropis. Di kawasan Mediterania seperti Yunani dan Italia, iklimnya hangat. Musim panasnya kering sementara musim dinginnya basah. Iklim subtropis punya curah hujan yang sedang sepanjang tahun.')
    elif message2 == 'iklim sedang':
        await ctx.send('iklim sedang atau iklim siklon dapat dijumpai di bumi belahan Utara atau Utara garis khatulistiwa. Di kawasan ini, kutub yang dingin bertemu dengan udara yang hangat. Hasilnya, hujan dan salju kerap ditemui di kawasan beriklim sedang. Iklim subtropis menghasilkan suhu musiman yang beragam. Umumnya ada empat musim, yakni musim panas, musim gugur, musim dingin, dan musim semi.')
    elif message2 == 'iklim dingin':
        await ctx.send('Iklim dingin ada di kutub bumi yakni kutub utara dan kutub selatan. Di kedua wilayah ini, musim dingin terjadi sepanjang tahun. Di beberapa area bahkan suhu yang selalu di bawah nol derajat celcius atau membeku. Sebagian tempat memiliki salju dan es. Di tempat lain, lapisan tanah bawahnya membeku.')
    elif message2 == 'iklim fisis':
        await ctx.send('menurut keadaan atau fakta sesungguhnya di suatu wilayah muka bumi sebagai hasil pengaruh lingkungan alam yang terdapat di wilayah tersebut.')

    else:
        await ctx.send('perintah itu gak ada')

@bot.command()
async def informasi_cuaca(ctx):
    await ctx.send(f'silahkan memilih cuaca apa yang ingin anda ketahui(jangan pakai tanda dolar):' )
    await ctx.send(f'\n-hujan \n-panas \n-berawan \n-hujan \n-salju \n-badai petir \n-hujan es \n-kabut \n-dingin \n-angin kencang \n-tornado \n-siklon tropis' )
    message = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    message = str(message.content)

    if message == 'cerah':
        await ctx.send('Cuaca yang terjadi saat langit cerah tanpa awan yang signifikan. Matahari bersinar terang dan cuaca umumnya hangat.')
    elif message == 'berawan':
        await ctx.send('Cuaca yang ditandai oleh kehadiran awan yang menutupi langit. Meskipun tidak terlalu cerah, biasanya tidak ada hujan atau salju yang turun.')
    elif message == 'hujan':
        await ctx.send('Cuaca di mana air turun dari langit dalam bentuk tetesan air. Hujan dapat bervariasi dari gerimis ringan hingga hujan deras.')
    elif message == 'salju':
        await ctx.send('Cuaca di mana air turun dari langit dalam bentuk kristal es. Salju sering terjadi di daerah dengan suhu rendah dan dapat menyebabkan penumpukan lapisan salju di permukaan tanah.')
    elif message == 'badai petir':
        await ctx.send('Cuaca yang ditandai oleh kilat, guntur, dan hujan yang intens. Badai petir biasanya terjadi dalam kondisi yang lembap dan dapat disertai dengan angin kencang.')
    elif message == 'hujan es':
        await ctx.send('Cuaca di mana es yang terbentuk dalam awan turun sebagai butiran es. Hujan es dapat menyebabkan kerusakan pada tanaman, kendaraan, dan struktur bangunan.')
    elif message == 'kabut':
        await ctx.send(' Cuaca di mana partikel air mengisi udara dan mengurangi jarak pandang. Kabut biasanya terjadi saat kelembapan tinggi dan suhu rendah.')
    elif message == 'panas':
        await ctx.send('Cuaca yang ditandai oleh suhu tinggi di atas normal. Panas yang ekstrem dapat berbahaya bagi kesehatan dan memicu gelombang panas.')
    elif message == 'dingin':
        await ctx.send('Cuaca dengan suhu rendah di bawah normal. Dingin yang ekstrem dapat menyebabkan kondisi beku dan berbahaya bagi kesehatan.')
    elif message == 'angin kencang':
        await ctx.send('Cuaca di mana angin berhembus dengan kecepatan yang tinggi. Angin kencang dapat menyebabkan kerusakan pada bangunan dan pohon, serta mempengaruhi transportasi.')
    elif message == 'tornado':
        await ctx.send('Cuaca yang ditandai oleh terbentuknya pusaran angin yang kuat dan berputar dengan kecepatan tinggi. Tornado biasanya disertai hujan dan awan yang khas.')
    elif message == 'siklon tropis':
        await ctx.send('Cuaca ekstrem melibatkan pergerakan besar udara dengan kecepatan tinggi yang berpusat di sekitar mata siklon. Siklon tropis dapat menyebabkan hujan lebat, banjir, angin kencang, dan gelombang laut yang tinggi.')

    else:
        await ctx.send('perintah tidak di temukan')

@bot.command()
async def pengertian_cuaca(ctx):
    await ctx.send(f'Cuaca adalah keadaan atmosfer di suatu tempat pada saat tertentu. Ini mencakup berbagai elemen seperti suhu udara, kelembaban, angin, dan kondisi langit. Sementara menurut KKBI, cuaca adalah keadaan udara (tentang suhu, cahaya matahari kelembapan, kecepatan angin, dan sebagainya) pada satu tempat tertentu dengan jangka waktu terbatas.')

@bot.command()
async def pengertian_iklim(ctx):
    await ctx.send(f'Iklim adalah pola dalam pengertian cuaca jangka panjang pada daerah tertentu. Cuaca dapat berubah dari jam ke jam, hari ke hari, bulan ke bulan atau bahkan tahun ke tahun. Pola cuaca suatu wilayah, biasanya dilacak selama setidaknya 30 tahun yang dianggap sebagai iklim.')

@bot.command()
async def penyebab_perubahan_iklim(ctx):
    await ctx.send(f'Emisi gas rumah kaca menyelimuti Bumi dan memerangkap panas matahari. Hal ini menyebabkan pemanasan global dan perubahan iklim. Saat ini, dunia mengalami pemanasan tercepat dalam sejarah.')

@bot.command()
async def solusi_mencegah_perubahan_iklim(ctx):
    await ctx.send(f'Solusi dasar dari perubahan iklim adalah untuk mengurangi emisi gas rumah kaca seminimal mungkin. Karena hutan dan lautan memainkan peran yang penting dalam mengatur iklim, meningkatkan kemampuan alami hutan dan lautan untuk menyerap karbon dapat membantu mengurangi efek dari pemanasan global.')

@bot.command()
async def help_command(ctx):
    await ctx.send('berikut perintah-perintah yang bisa di gunakan untuk menjalakan botnya:')
    await ctx.send(f'\n-halo \n-informasi_cuaca \n-pengertian_iklim \n-penyebab_perubahan_iklim \n-solusi_mencegah_perubahan_iklim \n-cek_cuaca \n-arti_cuaca \n-cek_derajat')
    await ctx.send('jangan lupa di simpan agar tidak lupa :)')

@bot.command()
async def cek_cuaca(ctx):
    API_KEY = '4d2d6fcf3333ddf73f72ea94251cb69b'
    await ctx.send('Masukkan nama Kota')
    kota = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    kota = str(kota.content)
    data_kota = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={kota}&limit=1&appid={API_KEY}')
    new_kota = data_kota.json()
    lat, lon = new_kota[0]['lat'], new_kota[0]['lon']

    cuaca_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}')
    data = cuaca_data.json()
    cuaca = data['weather'][0]['main']
    await ctx.send(f'cuaca di {kota} adalah {cuaca}')

@bot.command()
async def arti_cuaca(ctx):
    await ctx.send('berikut arti-artinya:')
    await ctx.send(f'\n-Sunny: Cerah \n-Cloudy: Berawan \n-Rainy: Hujan \n-Windy: Angin kencang \n-Stormy: Badai \n-Snowy: Bersalju \n-Foggy: Berkabut \n-Clear: Langit bening tanpa awan \n-Misty: Kabut tipis \n-Humid: Lembap \n-Wet: Basah \n-Bloom: Bersemi \n-Bright: Terang \n-Cool: Sejuk \n-Gloomy: Gelap \n-Dry: Cuaca kering tanpa hujan \n-Hot: Panas, suhu udara tinggi \n-Cold: Dingin, suhu udara rendah \n-Freezing: Pekat, suhu udara sangat rendah sehingga dapat membekukan air \n-Breezy: Sejuk berangin, sepoi-sepoi \n-Overcast: Langit sepenuhnya tertutup awan \n-Chilly: Dingin sekali, suhu udara dingin tapi tidak sampai membeku \n-Mild: Sedang, cuaca dengan suhu yang tidak terlalu panas atau terlalu dingin \n-Drizzle: Gerimis, hujan ringan dan halus \n-Blizzard: Badai salju, hujan salju intens dengan angin kencang dan penglihatan yang sangat terbatas\n-Hazy: Berawan tebal, udara yang terasa keruh dan terlihat kabur akibat partikel-partikel kecil \n-Sweltering: Panas menyengat, suhu yang sangat tinggi dan membuat sangat panas \n-Sleet: Hujan salju cair, hujan yang terdiri dari campuran salju dan air hujan \n-Frosty: Dingin berkabut, udara sangat dingin sehingga menyebabkan embun beku pada permukaan \n-Tropical: Tropis, cuaca yang khas tropis dengan suhu hangat sepanjang tahun \n-Muggy: Lembap dan panas, udara yang lembab dan panas secara bersamaan \n-Gusty: Angin kencang tidak terduga \n-Partly Cloudy: Sebagian berawan \n-Arid: Kering dan gersang \n-Mild Fog: Kabut ringan, kabut tipis yang terjadi dengan tingkat kepadatan yang lebih rendah')
    await ctx.send('jangan lupa di simpan agar tidak lupa :)')

@bot.command()
async def cek_derajat(ctx):
    API_KEY = '4d2d6fcf3333ddf73f72ea94251cb69b'
    await ctx.send('Masukkan nama Kota')
    kota = await bot.wait_for('message', check=lambda m: m.author == ctx.author and m.channel == ctx.channel)
    kota = str(kota.content)
    data_kota = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={kota}&limit=1&appid={API_KEY}')
    new_kota = data_kota.json()
    lat, lon = new_kota[0]['lat'], new_kota[0]['lon']

    suhu_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}')
    data = suhu_data.json()
    suhu = data['main']['temp']
    await ctx.send(f'suhu di {kota} adalah {round(suhu)-237}°C')

bot.run("MTI2NTI4Mzc5ODIyNDg2MzI5Mw.G5ScxV.qhBZ7xocVq1q6-u2yCTXIiCbfdjIr_fov9oqgs")
