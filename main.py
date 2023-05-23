import nextcord
from nextcord.ext import commands
import time
from datetime import *
import sqlite3
import random
import os



def logfile(text):
    with open('log.txt', 'a') as f:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        f.writelines('[{}] {} \n'.format(dt_string, text))
        f.close()

client = commands.Bot(command_prefix='$', help_command=None, intents=nextcord.Intents.all())
now = datetime.now()

print('+------------------------+')
print('| connected to sensei.db |')
print('+------------------------+')
con = sqlite3.connect('sensei.db')
c = con.cursor()
bot = client
bot.t = 0
bot.seal = 0
from webserver import keep_alive
import os
c.execute('CREATE TABLE IF NOT EXISTS claimed_cards(name_card TEXT, img TEXT, rank TEXT, id INTEGER, author TEXT)')


def restore():
    for x,y in k.items():
        c.execute('CREATE TABLE IF NOT EXISTS names(name TEXT, img TEXT, rank TEXT)')
        c.execute('INSERT INTO names( name, img, rank) VALUES(?, ?, ?)', (x, y, 'D'))
        con.commit()
        print(f'added {x} and {y} into the database with rank D')

    for x,y in k.items():
        c.execute('CREATE TABLE IF NOT EXISTS names(name TEXT, img TEXT, rank TEXT)')
        c.execute('INSERT INTO names( name, img, rank) VALUES(?, ?, ?)', (x, y, 'C'))
        con.commit()
        print(f'added {x} and {y} into the database with rank C')

    for x,y in k.items():
        c.execute('CREATE TABLE IF NOT EXISTS names(name TEXT, img TEXT, rank TEXT)')
        c.execute('INSERT INTO names( name, img, rank) VALUES(?, ?, ?)', (x, y, 'B'))
        con.commit()
        print(f'added {x} and {y} into the database with rank B')

    for x,y in k.items():
        c.execute('CREATE TABLE IF NOT EXISTS names(name TEXT, img TEXT, rank TEXT)')
        c.execute('INSERT INTO names( name, img, rank) VALUES(?, ?, ?)', (x, y, 'a'))
        con.commit()
        print(f'added {x} and {y} into the database with rank A')

    for x,y in k.items():
        c.execute('CREATE TABLE IF NOT EXISTS names(name TEXT, img TEXT, rank TEXT)')
        c.execute('INSERT INTO names( name, img, rank) VALUES(?, ?, ?)', (x, y, 'S'))
        con.commit()
        print(f'added {x} and {y} with rank into the database with rank S')

class step2(nextcord.ui.View):
    @nextcord.ui.button(label='⏭️ next step', style=nextcord.ButtonStyle.blurple)
    async def close(self, button : nextcord.ui.button, interaction: nextcord.Interaction):
        channel = interaction.channel
        await bot.stap1.delete()
        y = nextcord.Embed(color=0x000000)
        y.set_author(name='step 2 of the tutorial')
        y.add_field(name='how do u see which characters you have?', value='u can use **$inv** or **$inventory**  to see what you have the ranks go from a to s were a is the lowest rank and s the best rank!')
        y.set_image(url='https://cdn.discordapp.com/attachments/943475825930543144/950719058662273084/unknown.png')
        bot.stap2 = await channel.send(embed=y, view=step3())

class step3(nextcord.ui.View):
    @nextcord.ui.button(label='⏭️ next step', style=nextcord.ButtonStyle.blurple)
    async def close(self, button : nextcord.ui.button, interaction: nextcord.Interaction):
        channel = interaction.channel
        await bot.stap2.delete()
        y = nextcord.Embed(color=0x000000)
        y.set_author(name='step 3 of the tutorial.')
        y.add_field(name='the bot also has an economy system which has a currency the currency is ryo!', value='You have several ways to gain money we will be going over that in the next step, \n to see your current balance use $balance.')
        bot.stap3 = await channel.send(embed=y, view=step4())

class step4(nextcord.ui.View):
    @nextcord.ui.button(label='⏭️ next step', style=nextcord.ButtonStyle.blurple)
    async def close(self, button : nextcord.ui.button, interaction: nextcord.Interaction):
        channel  = interaction.channel
        await bot.stap3.delete()
        y = nextcord.Embed(color=0x000000)
        y.set_author(name='step 4 of the tutorial')
        y.add_field(name='ways of getting money!', value='you have several ways to make money, you can either use the $daily command with an 24 hour cooldown \n you also have $protect which gives an random amount of money give by the village you protect \n you can also sell a claimed card using the command $sell  ')
        bot.stap4 = await channel.send(embed=y, view=step5())


class step5(nextcord.ui.View):
    @nextcord.ui.button(label='❌ close ', style=nextcord.ButtonStyle.blurple)
    async def close(self, button : nextcord.ui.button, interaction: nextcord.Interaction):
        await bot.stap4.delete()

k = {
    'madara uchiha' : 'https://cdn.discordapp.com/attachments/943153914210025484/943412597175255070/2Q.png',
    'obito uchiha' : 'https://cdn.discordapp.com/attachments/943153914210025484/943412672362332180/OIP.png',
    'naruto uzumaki' :' https://cdn.discordapp.com/attachments/943153914210025484/943165034907967558/OIP.png',
    'sakura haruno' : 'https://cdn.discordapp.com/attachments/943153914210025484/943165056395407371/2Q.png',
    'sasuke uchiha' : 'https://cdn.discordapp.com/attachments/943153914210025484/943165072073691136/OIP.png',
    'kakashi hatake' : 'https://cdn.discordapp.com/attachments/943153914210025484/943165090625093652/OIP.png',
    'itachi uchiha' : 'https://cdn.discordapp.com/attachments/943153914210025484/943165120492732416/OIP.png',
    'boruto uzumaki' : 'https://cdn.discordapp.com/attachments/943153914210025484/943165144651927612/OIP.png',
    'sarada uchiha' : 'https://cdn.discordapp.com/attachments/943153914210025484/943165172594401280/OIP.png',
    'mitsuki' : 'https://cdn.discordapp.com/attachments/943153914210025484/943165187698085948/Z.png',
    'rock lee' : 'https://cdn.discordapp.com/attachments/943153914210025484/943165211207172127/OIP.png',
    'metal lee' : 'https://cdn.discordapp.com/attachments/943153914210025484/943165232879112293/OIP.png',
    'tenten' : 'https://cdn.discordapp.com/attachments/943153914210025484/943165247794081882/OIP.png',
    'orochimaru' : 'https://cdn.discordapp.com/attachments/943153914210025484/943165265196244992/OIP.png',
    'ino yamanaka' : 'https://cdn.discordapp.com/attachments/943153914210025484/943165281298165840/OIP.png',
    'choji akimichi' : 'https://cdn.discordapp.com/attachments/943153914210025484/943165297198792734/OIP.png',
    'shikamaru nara' : 'https://cdn.discordapp.com/attachments/943153914210025484/943165319311134729/OIP.png',
    'shikadai nara' : 'https://cdn.discordapp.com/attachments/943153914210025484/943165338495881306/OIP.png',
    'chocho akimichi' : 'https://cdn.discordapp.com/attachments/943153914210025484/943165353238855730/9k.png',
    'gaara' : 'https://cdn.discordapp.com/attachments/943153914210025484/943365259861831690/OIP.png',
    'temari' : 'https://cdn.discordapp.com/attachments/943153914210025484/943365302434017291/OIP.png',
    'kankuro' : 'https://cdn.discordapp.com/attachments/943153914210025484/943365331160801310/OIP.png',
    'sai' : 'https://cdn.discordapp.com/attachments/943153914210025484/943365352795013160/OIP.png',
    'hindan' : 'https://cdn.discordapp.com/attachments/943153914210025484/943412700590006282/OIP.png',
    'konan' : 'https://cdn.discordapp.com/attachments/943153914210025484/943412724157775902/OIP.png',
    'yahiko' : 'https://cdn.discordapp.com/attachments/943153914210025484/943412743518683167/OIP.png',
    'nagato uzumaki' : 'https://cdn.discordapp.com/attachments/943153914210025484/943412768927809576/OIP.png',
    'deidara' : 'https://cdn.discordapp.com/attachments/943153914210025484/943412837911523328/OIP.png',
    'sasori' : 'https://cdn.discordapp.com/attachments/943153914210025484/943412855376609290/OIP.png',
    'kakuzu' : 'https://cdn.discordapp.com/attachments/943153914210025484/943412871344324649/OIP.png',
    'hinata hyuga' : 'https://cdn.discordapp.com/attachments/943153914210025484/943412886502527016/OIP.png',
    'kiba inuzaka' : 'https://cdn.discordapp.com/attachments/943153914210025484/943412910728810506/OIP.png',
    'himawari uzumaki' : 'https://cdn.discordapp.com/attachments/943153914210025484/943412938813874226/OIP.png',
    'killer bee' : 'https://cdn.discordapp.com/attachments/943153914210025484/943412954659967006/OIP.png',
    'zabuza momochi' : 'https://cdn.discordapp.com/attachments/943153914210025484/943412978810765343/OIP.png',
    'haku' : 'https://cdn.discordapp.com/attachments/943153914210025484/943413190925115422/2Q.png',
    'hashirama senju' : 'https://cdn.discordapp.com/attachments/943153914210025484/943413209526861834/OIP.png',
    'minato namikaze' : 'https://cdn.discordapp.com/attachments/943153914210025484/943413233514070026/OIP.png',
    'tobirama senju' : 'https://cdn.discordapp.com/attachments/943153914210025484/943413270885330994/OIP.png',
    'hiruzen sarutobi' : 'https://cdn.discordapp.com/attachments/943153914210025484/943413347024506900/OIP.png',
    'kushina uzumaki' : 'https://cdn.discordapp.com/attachments/943153914210025484/943413368033804319/OIP.png',
    'indra otsutsuki' :'https://cdn.discordapp.com/attachments/943153914210025484/943413384643231785/OIP.png',
    'asura otsutsuki' : 'https://cdn.discordapp.com/attachments/943153914210025484/943413403614064730/OIP.png',
    'boro' : 'https://cdn.discordapp.com/attachments/943153914210025484/943413663434416188/OIP.png',
    'zetsu' : 'https://cdn.discordapp.com/attachments/943153914210025484/943413664579457034/OIP.png',
    'jigen' : 'https://cdn.discordapp.com/attachments/943153914210025484/943413664411713566/Z.png',
    'hagoromo otsutsuki' : 'https://cdn.discordapp.com/attachments/943153914210025484/943413664474615818/OIP.png',
    'toneri otsutsuki' : 'https://cdn.discordapp.com/attachments/943153914210025484/943413664290066473/OIP.png',
    'delta' : 'https://cdn.discordapp.com/attachments/943153914210025484/943413664688513024/OIP.png',
    'kaguya otsutsuki' : 'https://cdn.discordapp.com/attachments/943153914210025484/943413664445263882/OIP.png',
    'momoshiki otsutsuki' : 'https://cdn.discordapp.com/attachments/943153914210025484/943413664717873152/OIP.png',
    'kinshiki otsutsuki' : 'https://cdn.discordapp.com/attachments/943153914210025484/943413665682571314/OIP.png',
    'kashin koji' : 'https://cdn.discordapp.com/attachments/943153914210025484/943413723572363274/OIP.png',
    'yamato' : 'https://cdn.discordapp.com/attachments/943153914210025484/943413785341882368/OIP.png',
    'hamura otsutsuki' : 'https://cdn.discordapp.com/attachments/943153914210025484/943413989814173726/OIP.png',
    'neji hyuga' : 'https://cdn.discordapp.com/attachments/943153914210025484/943413990204243968/OIP.png',
    'danzo shimura' : 'https://cdn.discordapp.com/attachments/943153914210025484/943413990443343912/OIP.png',

}
def idinsertion():
    for item,link in k.items():
        id = random.randint(100000, 999999)
        c.execute('CREATE TABLE IF NOT EXISTS idbycharacter(name TEXT, discord_link TEXT, id TEXT)')
        c.execute('INSERT INTO idbycharacter(name, discord_link, id) VALUES(?, ?, ?)', (item, link, id))
        print(f'inserted {item}, {link}, {id}')
        con.commit()


all_role={
    'Uchiha' : 100000,
    'Otsutsuki' : 110000,
    'Hyuga' : 90000,
    'Uzumaki' : 100000,
    'Senju' : 100000,
    'Lightning Release' : 5000,
    'Water Release' : 5000,
    'Fire Release' : 5000,
    'Earth Release' : 5000,
    'Wind Release' : 5000,
    'Flying Rajin' : 5000,
    'Drunken Fist' : 5000,
    'Sand Coffin' : 5000,
    'Byakugan' : 7500,
    'Ketsuryugan' : 7500,
    'Kotoamatsukami' : 20000,
    'Tenseigan' : 15000,
    'Jougan' : 15000,
    'Sharingan' : 10000,
    'Sagemode' : 25000,
    'Izanami' : 50000,
    'Izanagi' : 50000,
    'Eight Gates' : 45000,
    'Susanoo' : 35000,
    'Tailed Beast Bomb' : 30000,
    'Rasengan' : 10000,
    'Amaterasu' : 15000,
    'Chibaku Tensei' : 15000,
    'Chidori' : 10000,
    'Six Paths of Pain' : 45000,
    'Tsukuyomi' : 30000,
    'Rinnegan' : 30000,
    'Summoning Jutsu' : 40000,
}

clan_role={
    'Uchiha' : 100000,
    'Otsutsuki' : 110000,
    'Hyuga' : 90000,
    'Uzumaki' : 100000,
    'Senju' : 100000
}

showcase_roles={
    'Lightning Release' : 5000,
    'Water Release' : 5000,
    'Fire Release' : 5000,
    'Earth Release' : 5000,
    'Wind Release' : 5000,
    'Flying Rajin' : 5000,
    'Drunken Fist' : 5000,
    'Sand Coffin' : 5000,
    'Byakugan' : 7500,
    'Ketsuryugan' : 7500,
    'Kotoamatsukami' : 20000,
    'Tenseigan' : 15000,
    'Jougan' : 15000,
    'Kamui' : 25000
    }

p = {
    'Sharingan' : 10000,
    'Sagemode' : 25000,
    'Izanami' : 50000,
    'Izanagi' : 50000,
    'Eight Gates' : 45000,
    'Susanoo' : 35000,
    'Tailed Beast Bomb' : 30000,
    'Rasengan' : 10000,
    'Amaterasu' : 15000,
    'Chibaku Tensei' : 15000,
    'Chidori' : 10000,
    'Six Paths of Pain' : 45000,
    'Tsukuyomi' : 30000,
    'Rinnegan' : 30000,
    'Summoning Jutsu' : 40000,
}



@client.command()
async def createroles(ctx):
    guild = ctx.guild
    for item in all_role.items():
        await guild.create_role(name=f"{item[0]}")
        user = nextcord.get_user_by_id(958265660427878441)
        await user.add_role(role = role)
        role = print(f'created role with the name {item}')
        await ctx.send(f'created role with name {item[0]}')
        print(repr(role))


@client.command()
async def tutorial(ctx):

    author = ctx.author
    message = ctx.message
    logfile(f'{author.name} has used the tutorial command')
    await message.delete()
    t = nextcord.Embed(color=0x000000)
    t.set_author(name=f'welcome to the tutorial {author.name} \n press ⏭️ to go to the next step')
    bot.stap0 = await ctx.send(embed=t, view=step1())

class step1(nextcord.ui.View):
    @nextcord.ui.button(label='⏭️ next step', style=nextcord.ButtonStyle.blurple)
    async def close(self, button : nextcord.ui.button, interaction: nextcord.Interaction):
        channel = interaction.channel
        await bot.stap0.delete()
        y = nextcord.Embed(color=0x000000)
        y.set_author(name='step 1 of the tutorial')
        y.add_field(name='how does the bot work?', value='when 20 messages has been sended the bot will send a random picture from a naruto character u can type: **$claim ** to claim the character')
        y.set_image(url='https://cdn.discordapp.com/attachments/943475825930543144/950718485384806430/unknown.png')
        y.set_image(url='https://cdn.discordapp.com/attachments/943475825930543144/950719313403326464/unknown.png')
        bot.stap1 = await channel.send(embed=y, view=step2())

@client.event
async def on_ready():
    print('+----------------------+')
    print(f'| bot is ready        |')
    print('+----------------------+')
    print('\n')
    await client.change_presence(activity=nextcord.Activity(type=nextcord.ActivityType.playing, name="Training in Konohagakure!"))

@client.event
async def on_message(message):
    if message.author.bot == False:
        bot.t += 1
        t = 20 - bot.t
        print('+---------------------------------------------------+')
        print(f'| message number {bot.t} another {t} more for a picture |')
        print('+---------------------------------------------------+')
        if bot.t == 20:
            channel1 = message.channel
            item1 = random.choice(list(k.values()))
            t = nextcord.Embed(color=0x000000)
            t.set_image(url=item1)
            t.set_footer(text='Type kg!claim  to claim it! ')
            if message.channel != 952668238444126259:
                await channel1.send(embed=t)
            else:
                return
            bot.t = 0
            bot.name = (next((key for key, value in k.items() if value == item1), None))
            print('\n')
            print('+----------------------------------------------+')
            print("the correct gues is "+ f"'{bot.name}'")
            print('+----------------------------------------------+')
    await client.process_commands(message)


def reroll():
    bot.name = random.choice(list(k.values()))
p=(['D', 'C', 'B', 'A', 'S'], [50, 20, 20, 9.99, 0.001])
@client.command(aliases=['C', 'c'])
async def claim(ctx, *, guess):
    print('a')
    ryo=([30, 40, 50, 60, 70], [40, 20, 10, 7.5, 2.5])
    print('q')
    bot.u = bot.name
    author = ctx.author.name
    if bot.u == guess:
        rank = random.choices(*p)
        print(f'{rank} : {bot.u}')
        money = random.randint(0, 150)
        # inserting the 40 money
        c.execute('CREATE TABLE IF NOT EXISTS balances(username text, balance int, id int)')

        c.execute('SELECT * FROM balances WHERE username = ?', (author,))
        print('a')
        list1 = c.fetchone()
        print(list1)
        if list1 is None:
            balance = 0
            print('created table')
            newbalance = balance + money
            c.execute('INSERT INTO balances(username, balance) VALUES(?, ?)', (author, newbalance))

        else:
            newbalance = list1[1] + money
            c.execute('UPDATE balances SET balance = ? WHERE username = ?', (newbalance, author))

        con.commit()
        # inserting the name + rank
        c.execute('SELECT * FROM idbycharacter WHERE  name = ?', (bot.u,))
        idfetch = c.fetchone()
        if idfetch is None:
            id = 999999
        else:
            id = idfetch[2]
        c.execute(f'INSERT INTO claimed_cards(name_card, rank, id, author) VALUES(?, ?, ?, ?)', (bot.u, rank[0], id, author))
        t = nextcord.Embed(color=0x000000)
        mention = ctx.author.mention
        t.add_field(value=f'{mention} has succesfully claimed a **{rank[0]}** rank **{bot.name}** and u received a addintional {money} ryo', name='claimed ✅')
        reroll()
        con.commit()
        await ctx.send(embed=t)
        print('+------------------------------------+')
        print(f'| {author} has guessed {bot.u} |')
        print('+------------------------------------+')
        
    else:
        mention = ctx.author.mention
        t= nextcord.Embed(color=0x000000)
        t.add_field(value=f'{mention} this guess is wrong', name='not claimed  ❌')
        await ctx.send(embed= t)
        con.commit()



@client.command(aliases=['inv'])
async def inventory(ctx, player=None):
    now = datetime.now()
    dt_string = now.strftime("%H:%M:%S")
    db = ctx.author.name
    if player == None:
        player = ctx.author.name
    t = nextcord.Embed(color=0x000000)
    t.set_author(name=f'inventory of {player} ')
    t.set_footer(text=f'{dt_string}')
    c.execute("SELECT * FROM claimed_cards where author = ?", (player,))
    data = c.fetchall()
    t.add_field(name='+---------------------------------------------+', value='\u200b', inline=False)
    for item in data:
        print(item)
        t.add_field(name='\u200b', value=f"** `{item[2]}` rank `{item[0]}` with id `{item[3]}`**", inline=False)
    t.add_field(name='+---------------------------------------------+', value='\u200b', inline=False)
    await ctx.send(embed = t)
    print('+---------------------------------+')
    print(f'| {db} has accesed his inventory |')
    print('+---------------------------------+')


@client.command(description='lets u do a suggestion')
async def suggest(ctx, *, suggestion):
    now = datetime.now()
    dt_string = now.strftime("%H:%M:%S")
    author = ctx.author
    channel = client.get_channel(948886537100210216)
    y = nextcord.Embed(color=0x000000)
    y.set_author(name=f'suggestion of {author.name}')
    y.add_field(name='suggestion:', value=f'{suggestion}')
    y.set_footer(text=f'{dt_string}')
    await channel.send(embed = y)

class shop1(nextcord.ui.View):
    @nextcord.ui.button(label='🤑 Ryo Roles', style=nextcord.ButtonStyle.blurple)
    async def close3(self, button : nextcord.ui.button, interaction: nextcord.Interaction):
            channel = interaction.channel
            y = nextcord.Embed(color=0x000000)
            y.set_author(name='Ryo Roles')
            y.add_field(name='item  -------------- price', value='\u200b')
            y.add_field(name='Sharingan - 10,000 Ryo ', value='```id = sharigan```', inline=False)
            y.add_field(name='Sagemode - 25,000 Ryo', value='```id = sagemode```', inline=False)
            y.add_field(name='Izanami - 50,000 Ryo', value='```id = izanami```', inline=False)
            y.add_field(name='Izanagi - 50,000 Ryo', value='```id = izanagi```', inline=False)
            y.add_field(name='Eight Gates - 45,000 Ryo', value='```id = eight_gates```', inline=False)
            y.add_field(name='Susanoo - 35,000 Ryo', value='```id = susanoo```', inline=False)
            y.add_field(name='Tailed Beast Bomb - 30,000 Ryo', value='```id = tailed_beast_bomb```', inline=False)
            y.add_field(name='Rasengan - 10,000 Ryo', value='```id = rasegan```', inline=False)
            y.add_field(name='Amaterasu - 15,000 Ryo', value='```id = amaterasu```', inline=False)
            y.add_field(name='Chibaku Tensei - 15,000 Ryo', value='```id = chibaku tensei```', inline=False)
            y.add_field(name='Chidori - 10,000 Ryo', value='```id = chidori```', inline=False)
            y.add_field(name='Six Paths of Pain - 45,000 Ryo', value='```id = six_paths_of_pain```', inline=False)
            y.add_field(name='Tsukuyomi - 30,000 Ryo', value='```id = tsukuyomi```', inline=False)
            y.add_field(name='Rinnegan - 30,000 Ryo', value='```id = rinnegan```', inline=False)
            y.add_field(name='Summoning Jutsu - 40,000 Ryo', value='```id = summoning_jutsu```', inline=False)
            y.set_footer(text='if u want to buy something make sure to use the exact item name with capitals')
            bot.n=  await channel.send(embed = y)


    @nextcord.ui.button(label='🏅 Showcase Roles', style=nextcord.ButtonStyle.blurple)
    async def close2(self, button : nextcord.ui.button, interaction: nextcord.Interaction):
            channel = interaction.channel
            y = nextcord.Embed(color=0x000000)
            y.set_author(name='🏅 Showcase Roles')
            y.add_field(name='Lightning Release - 5,000 Ryo', value='```id = lightning_release```', inline=False)
            y.add_field(name='Water Release - 5,000 Ryo', value='```id = water_release```', inline=False)
            y.add_field(name='Fire Release - 5,000 Ryo', value='```id = fire_release```', inline=False)
            y.add_field(name='Earth Release - 5,000 Ryo', value='```id = earth_release```', inline=False)
            y.add_field(name='Wind Release - 5,000 Ryo', value='```id = wind_release```', inline=False)
            y.add_field(name='Flying Rajin - 5,000 Ryo', value='```id = flying_rajin```', inline=False)
            y.add_field(name='Drunken Fist - 5,000 Ryo', value='```id = drunken_fist```', inline=False)
            y.add_field(name='Sand Coffin - 5,000 Ryo', value='```id = sand_coffin```', inline=False)
            y.add_field(name='Byakugan - 7,500 Ryo', value='```id = byakugan```', inline=False)
            y.add_field(name='Ketsuryugan - 7,500 Ryo', value='```id = ketsuryugan```', inline=False)
            y.add_field(name='Kotoamatsukami - 20,000 Ryo', value='```id = kotoamatsukami```', inline=False)
            y.add_field(name='Tenseigan - 15,000 Ryo', value='```id = tenseigan```', inline=False)
            y.add_field(name='Jougan - 15,000 Ryo', value='```id = jougan```', inline=False)
            y.set_footer(text='if u want to buy something make sure to use the exact item name with capitals')
            bot.b = await channel.send(embed = y)


    @nextcord.ui.button(label='🛡️ Clan Roles', style=nextcord.ButtonStyle.blurple)
    async def close1(self, button : nextcord.ui.button, interaction: nextcord.Interaction):
            channel = interaction.channel
            y = nextcord.Embed(color=0x000000)
            y.set_author(name='Clan Roles Shop ')
            y.add_field(name='Uchiha - 100,000 Ryo', value='```id = uchiha```', inline=False)
            y.add_field(name='Otsutsuki - 110,000 Ryo', value='```id = otsutsuki```', inline=False)
            y.add_field(name='Hyuga - 90,000 Ryo', value='```id = hyuga```', inline=False)
            y.add_field(name='Uzumaki - 100,000 Ryo', value='```id = uzumaki```', inline=False)
            y.add_field(name='Senju - 100,000 Ryo', value='```id = senju```', inline=False)
            y.set_footer(text='if u want to buy something make sure to use the exact item name with capitals')
            bot.v = await channel.send(embed = y)



@client.command(description='lets u see what u can buy ')
async def shop(ctx):
    author = ctx.author.name
    y = nextcord.Embed(color=0x000000)
    y.set_author(name=f'shop requested by {author}')
    y.add_field(name='click on one of the buttons do see the roles u can buy', value='\u200b')
    await ctx.send(embed=y, view=shop1())






@client.command(description='lets u see how much money u got', aliases=['bal', 'b'])
async def balance(ctx):
    author = ctx.author.name
    c.execute("SELECT * FROM balances WHERE username=?", (author,))
    list = c.fetchone()
    try:
        balance = list[1]
    except IndexError :
        balance = 0
    except TypeError:
        balance = 0
    y = nextcord.Embed(color=0x000000, description=f"{author}'s balance is {balance} ryo")
    #(value=f'the balance of {author} is {balance}', name='\u200b')
    await ctx.send(embed=y)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        timeinsec=error.retry_after
        timeinhour = timeinsec // 3600 
        timeinmin = (timeinsec % 3600) // 60
        print(timeinhour)
        timeinsec1 = ((timeinsec % 3600) // 60) % 60
        em = nextcord.Embed(title='u cant use this command yet', description=f'try again in {int(timeinsec1)} seconds {int(timeinmin)} minutes and {int(timeinhour)} hours', color=0xFF0000)
        await ctx.send(embed=em)
        return


    if isinstance(error, commands.MissingAnyRole):
        em = nextcord.Embed(title='u cant use this command yet', description='you haven\'t bought this command buy it using $buy ', color=0xFF0000)
        await ctx.send(embed = em)
        return

    else:
        user = client.get_user(786150856792735745)
        em = nextcord.Embed(title=f'bug report from {ctx.author}', description=f'{error}')
        await user.send(embed= em)
        logfile(f'[{error}]')


@client.command(description="lets u get some free money")
@commands.cooldown(1, 86400, commands.BucketType.user)
async def daily(ctx):
    author = ctx.author.name
    c.execute('CREATE TABLE IF NOT EXISTS balances(username text, balance int)')


    try:
        c.execute('SELECT * FROM balances WHERE username = ?', (author,))
        list1 = c.fetchone()

        if list1 is None:
            balance = 0
            print('created table')
            newbalance = balance + 150
            c.execute('INSERT INTO balances(username, balance) VALUES(?, ?)', (author, newbalance))
            con.commit()
            y = nextcord.Embed(color=0x000000, description='✅ u have succesfully claimed your daily reward!')
            await ctx.send(embed = y)
        else:
            newbalance = list1[1] + 1000
            c.execute('UPDATE balances SET balance = ? WHERE username = ?', (newbalance, author))
            con.commit()
            y = nextcord.Embed(color=0x000000, description='✅ u have succesfully claimed your daily reward!')
            await ctx.send(embed = y)
    except None:
        print('d')



class active_seals_switch(nextcord.ui.View):
    @nextcord.ui.button(label='❌ no', style=nextcord.ButtonStyle.blurple)
    async def close1(self, button : nextcord.ui.button, interaction: nextcord.Interaction):
        channel = interaction.channel
        await bot.a.delete()
        return

    @nextcord.ui.button(label=' ✅ yes', style=nextcord.ButtonStyle.blurple)
    async def close(self, button : nextcord.ui.button, interaction: nextcord.Interaction):
        channel = interaction.channel
        author = interaction.user.name
        opened_seal = bot.seal
        type(bot.seal)
        c.execute('UPDATE active_seals SET seal = ? WHERE name = ?', (bot.seal, author))
        await bot.a.delete()
        await channel.send(f'succesfully changed your active seal to {bot.seal}')


'''
@client.command(aliases=["rec"])
async def recruits(ctx, action="shop", rarity=None, amount=1):
    author = ctx.author.name
    if action == "shop":
        y = nextcord.Embed(color=0x000000)
        y.set_author(name='seal shop')
        y.add_field(name='common seal - **2000 ryo**', value='```$rec buy common_seal```', inline=False)
        y.add_field(name='rare seal - **10000 ryo**', value='```$rec buy rare_seal```', inline=False)
        y.add_field(name='epic seal - **25000 ryo**', value='```$rec buy epic_seal```', inline=False)
        y.add_field(name='legendary seal - **50000 ryo**', value='```$rec buy legendary_seal```', inline=False)
        y.set_footer(text='u can obtain mythic recruits by opening seals')
        await ctx.send(embed=y)

    if action == "buy":
        c.execute(f'CREATE TABLE IF NOT EXISTS active_seals(name TEXT, seal TEXT)')
        c.execute(f'CREATE TABLE IF NOT EXISTS claimed_cards(name TEXT, rank TEXT)')
        c.execute('SELECT * FROM balances WHERE username = ?', (author,))
        list1 = c.fetchone()
        if list1 is None:
            balance = 0
            newbalance = balance + 1000
            c.execute('INSERT INTO balances(username, balance) VALUES(?, ?)', (author, newbalance))
        else:
            if rarity == "common_seal":
                cost = 2000
                d = ['mei' , 'onoki' , 'a' , 'killer bee' , 'zetsu' , 'sai'  , 'tenten'  , 'haku' , 'sasori' ,' deidara' , 'danzo' ,]
            if rarity == "rare_seal":
                cost = 20000
                d=['shukaku' , 'matatabi' , 'kokuo' , 'son goku' , 'isobu' , 'konan' , 'yahiko' , 'tsunade' , 'hamura' , 'gaara' , 'kisame' ]
            if rarity == "epic_seal":
                cost = 250000
                d=[ 'hinata' , 'ino' , 'choji' , 'kiba' , 'shino' , 'saiken' , 'gyuki' , 'neji' , 'rock lee' , 'chomei' , 'nagato' , 'hagoromo']

            if rarity == "legendary_seal":
                d=['shikamaru' , 'madara' ,'itachi' , 'obito' , 'momoshiki' , 'isshiki' , 'kaguya' , 'jiraiya' , 'orochimaru' , 'minato' , 'kakashi' , 'guy' , 'jubi']
                cost = 50000
            opened_seal = random.choice(d)
            bot.seal = opened_seal
            newbalance = list1[1] - (cost * amount)
            if newbalance < 0:
                await ctx.send('u dont have enough money!')
                newbalance = list[1]
                return

            c.execute('UPDATE balances SET balance = ? WHERE username = ?', (newbalance, author))
            embed= nextcord.Embed(color=0x000000, title=f' 🎉 opening a {rarity} 🎉', description=f'you have gotten `{opened_seal}`')
            embed.set_footer(text='did you know that u can get an mythic with a chance of 0.00001 % by opening boxes')
            await ctx.send(embed=embed)
            c.execute('SELECT * FROM active_seals WHERE name = ?', (author,))
            list1 = c.fetchone()
            
            if list1 == None:
                c.execute(f'INSERT INTO active_seals(name, seal) VALUES(?, ?)', (author, opened_seal))

            else:
                bot.a = await ctx.send('do you wanna change ur active seal?', view=active_seals_switch())
            
            con.commit()
'''


@client.command()
async def protect(ctx):
    author = ctx.author.name
    c.execute('SELECT * FROM balances WHERE username = ?', (author,))
    list1 = c.fetchone()
    balance = list1[1]
    random_money = random.randint(1, 150)
    newbalance = balance + random_money
    if list1 == None:
        balance = 0
        newbalance = balance + random_money
        c.execute('INSERT INTO balances(username, balance) VALUES(?, ?)', (author, newbalance))
    else:
        c.execute('UPDATE balances SET balance = ? WHERE username = ?', (newbalance, author))
    await ctx.send(f' You successfully served as a bodyguard for the Hokage and gained `{random_money}` Ryo.')


@client.command(aliases=["cf"])
async def coinflip(ctx, ht, amount = None):
    author = ctx.author.name
    c.execute('SELECT * FROM balances WHERE username = ?', (author,))
    list1 = c.fetchone()
    balance = list1[1]
    hot = ["head", "tails"]
    gamble = random.choice(hot)
    
    if list1 is None:
        balance = 0
        newbalance = balance + amount
        c.execute('INSERT INTO balances(username, balance) VALUES(?, ?)', (author, newbalance))
        if (ht == "h" or ht =="head") and gamble == "h":
            await ctx.send('u have won with head!')
            return

        if (ht == "t" or ht == "tails") and gamble == "t":
            await ctx.send('u have won with tails!')
            return
        else:
            await ctx.send('u have lost D:')

        
        if (ht == "h" or ht =="head") and gamble == "h":
            await ctx.send('u have won with head!')
            c.execute('UPDATE balances SET balance = ? WHERE username = ?', (newbalance, author))
            return

        if (ht == "t" or ht == "tails") and gamble == "t":
            await ctx.send('You have won with tails!')
            c.execute('UPDATE balances SET balance = ? WHERE username = ?', (newbalance, author))
            return
        else:
            await ctx.send('You have lost!')
            c.execute('UPDATE balances SET balance = ? WHERE username = ?', (newbalance, author))
            return


class confirmation_buycmd(nextcord.ui.View):
    @nextcord.ui.button(label='❌ no', style=nextcord.ButtonStyle.blurple)
    async def close1(self, button : nextcord.ui.button, interaction: nextcord.Interaction):
        channel = interaction.channel
        await bot.b.delete()
        return

    @nextcord.ui.button(label=' ✅ yes', style=nextcord.ButtonStyle.blurple)
    async def close(self, button : nextcord.ui.button, interaction: nextcord.Interaction):
        channel = interaction.channel
        author = interaction.user.name
        new_balance = bot.g - bot.price
        if new_balance > 0:
                ranks = ['a', 'b', 'c', 'd', 's']
                rank = random.choice(ranks)
                c.execute(f'CREATE TABLE IF NOT EXISTS claimed_cards(name TEXT, rank TEXT, id TEXT)')
                c.execute(f'INSERT INTO claimed_cards(name, rank, id) VALUES(?, ?, ?)', (bot.cardinfo, rank, bot.id ))
                await channel.send(f'You have succesfully bought {bot.cardinfo} for {bot.price}!')
                await bot.b.delete()
        else:
            await channel.send('you don\'t have  enough money')


@client.command()
async def view(ctx, *, card):
    if card == None:
        await ctx.send('Make sure to put in a id!')
        return
    c.execute('SELECT * FROM idbycharacter WHERE id = ?', (card,))
    varfromdb = c.fetchone()
    if varfromdb == None:
        c.execute('SELECT * FROM idbycharacter where name =?', (card,))
        varfromdb = c.fetchone()
        if varfromdb is None:
            await ctx.send(f'The id `{id}` has not been found!')
            return

        else:
            embed = nextcord.Embed(color=0x000000, title=f'{varfromdb[0]}', description=f' `id = {varfromdb[2]}`')
            embed.set_image(url=f'{varfromdb[1]}')
            await ctx.send(embed=embed)
                    

@client.command()
async def market(ctx, action, *, id=None):
    if action =="view" or 'v':
                if id == None:
                    await ctx.send('Make sure to put in a id!')
                    return
                c.execute('SELECT * FROM idbycharacter WHERE id = ?', (id,))
                varfromdb = c.fetchone()
                if varfromdb == None:
                    c.execute('SELECT * FROM idbycharacter where name =?', (id,))
                    varfromdb = c.fetchone()
                    if varfromdb is None:
                        await ctx.send(f'the id `{id}` has not been found')
                        return

                else:
                    embed = nextcord.Embed(color=0x000000, title=f'{varfromdb[0]}', description=f' `{id}`')
                    embed.set_image(url=f'{varfromdb[1]}')
                    await ctx.send(embed=embed)
                    return
        
    if action == "buy" or "b":
            author = ctx.author.name
            c.execute('SELECT * FROM balances WHERE username = ?', (author,))
            balinfo = c.fetchone()
            if balinfo == None or balinfo[1] == 0:
                await ctx.send('You have no money try `$daily` or `$protect`!')
                return
            else:  
                c.execute('SELECT * FROM idbycharacter WHERE id = ?', (id,))
                cardinfo = c.fetchone()
                if cardinfo == None:
                    await ctx.send('Try to use a valid id!')
                    return
                else:
                    c.execute('SELECT * FROM balances WHERE username = ?', (author,))
                    balinfo = c.fetchone()
                    bot.id = id
                    bot.cardinfo = cardinfo[0]
                    bot.g = balinfo[1]
                    bot.price = random.randint(1, 1500)
                    bot.b = await ctx.send(f'The price of the card is `{bot.price}`.', view=confirmation_buycmd())
                    
                                                                                                                      
@client.command()
async def sell(ctx, price, *, name):
    author = ctx.author.name
    c.execute('CREATE TABLE IF NOT EXISTS marketplace(name TEXT, rank TEXT, id INTEGER, price INTEGER, seller TEXT, buy_id INTEGER)')
    c.execute(f'SELECT * FROM claimed_cards  where name = ?', (name,))
    invinfo = c.fetchone()
    if invinfo == None:
        await ctx.send('You cant sell that!')
        return
    else:
        c.execute(f'SELECT * FROM idbycharacter where name = ?', (name,))
        idfetch = c.fetchone()
        if idfetch == None:
            return
        buy_id=random.randint(1000000, 9999999)
        rank = invinfo[1]
        name = invinfo[0]
        id = idfetch[2]
        print(rank, name, id, price, author, buy_id)
        c.execute('INSERT INTO marketplace(name, rank, id, price, seller, buy_id) VALUES(?, ?, ?, ?, ?, ?)', (name, rank, id, price, author, buy_id))
        c.execute(f'DELETE FROM claimed_cards  where name = ? AND author = ?', (name, author,))
        await ctx.send(f'You have succesfully put `{name}` on the marketplace for `{price}`.')
        con.commit()

@client.command()
async def marketplace(ctx, action=None, id = None):
    author = ctx.author.name
    if action == "buy":
            c.execute('SELECT * FROM marketplace where buy_id = ?', (id,))
            item = c.fetchone()
            if item is None:
                c.execute('SELECT * FROM marketplace where  name = ?', (id,))
                item = c.fetchone()
                if item is None:
                    await ctx.send('There is no card with the id or name `{}`.'.format(id))
                    return
            c.execute('SELECT * FROM balances WHERE username = ?', (author,))
            balinfo = c.fetchone()
            if balinfo == None or balinfo[1] == 0:
                await ctx.send('u have no money try `$daily` or `$protect`')
                return
            test = balinfo[1] - item[3]
            if test <= 0:
                await ctx.send('u dont have enough money')
            else:
                new_balance = balinfo[1] - item[3]
                name = item[0]
                rank = item[1]
                id1 = item[2]
                c.execute('SELECT * FROM balances WHERE username = ?', (item[4],))
                balance_seller = c.fetchone()
                new_balance_seller = item[3] -balance_seller[1]
                c.execute('UPDATE balances SET balance = ? WHERE username = ?', (new_balance_seller, item[3]))
                c.execute('UPDATE balances SET balance = ? WHERE username = ?', (new_balance, author))
                c.execute(f'INSERT INTO claimed_cards(name_card, rank, id, author) VALUES(?, ?, ?, ?)', (name, rank, id1, author))
                c.execute(f'DELETE FROM marketplace  where buy_id = ?', (id,))
                await ctx.send(f'You have succesfully bought `{name}` with rank `{rank}` for `{item[3]}`, \n your new balance is `{new_balance}`!')
                con.commit()
                return
    if action == None:
        c.execute('CREATE TABLE IF NOT EXISTS marketplace(name TEXT, rank TEXT, id INTEGER, price INTEGER, seller TEXT, buy_id INTEGER)')
        marketplace = nextcord.Embed(color=0x000000, title='marketplace')
        c.execute('SELECT * FROM marketplace')
        stuff = c.fetchall()
        f = 0
        for item in stuff:
            try:
                marketplace.add_field(name=f'`{stuff[f][0]}`, \n rank : `{stuff[f][1]}`, \n price : `{stuff[f][3]}`, \n seller : `{stuff[f][4]}`, \n id : `{stuff[f][2]}`, \n buy id : `{stuff[f][5]}`', value='\u200b', inline=False)
                f +=1
            except IndexError:
                print('index error')    
    await ctx.send(embed=marketplace)
    con.commit()


'''
'Uchiha' : 100000,
    'Otsutsuki' : 110000,
    'Hyuga' : 90000,
    'Uzumaki' : 100000,
    'Senju' : 100000,
    'Lightning Release' : 5000,
    'Water Release' : 5000,
    'Fire Release' : 5000,
    'Earth Release' : 5000,
    'Wind Release' : 5000,
    'Flying Rajin' : 5000,
    'Drunken Fist' : 5000,
    'Sand Coffin' : 5000,
    'Byakugan' : 7500,
    'Ketsuryugan' : 7500,
    'Kotoamatsukami' : 20000,
    'Tenseigan' : 15000,
    'Jougan' : 15000,
    'Sharingan' : 10000,
    'Sagemode' : 25000,
    'Izanami' : 50000,
    'Izanagi' : 50000,
    'Eight Gates' : 45000,
    'Susanoo' : 35000,
    'Tailed Beast Bomb' : 30000,
    'Rasengan' : 10000,
    'Amaterasu' : 15000,
    'Chibaku Tensei' : 15000,
    'Chidori' : 10000,
    'Six Paths of Pain' : 45000,
    'Tsukuyomi' : 30000,
    'Rinnegan' : 30000,
    'Summoning Jutsu' : 40000,
'''



@client.command()
async def buy(ctx, *, id):
    guild = ctx.guild
    author = ctx.author.name
    price = random.randint(1, 150)
    rank = random.choices(*p)
    c.execute('SELECT * FROM balances WHERE username = ?', (author,))
    balancefetch = c.fetchone()
    if balancefetch is None:
        balance = 0
    else:
        balance = balancefetch[1]
    
    c.execute('SELECT * FROM  idbycharacter WHERE name = ?', (id,))
    characterfetch = c.fetchone()
    if characterfetch is not None:
        user = ctx.author
        id1 = characterfetch[3]  
        c.execute(f'INSERT INTO claimed_cards(name, rank, id) VALUES(?, ?, ?)', (id, rank, id1,))
        newbalance = balance - price
        price_difference = -newbalance
        return       

    else:
        c.execute('SELECT * FROM  idbyrole WHERE name = ?', (id,))
        rolefetch = c.fetchone()
        pricerole = rolefetch[2]
        newbalance = int(balance) - pricerole
        price_difference = newbalance

        if rolefetch is None:
            await ctx.send(f'There is no role or character with the name {id}.')
            await ctx.send('if u wanna buy a role remember to use CAPITALS! for example $buy Tsukoyomi')
            return
        else:
            role = nextcord.utils.get(ctx.guild.roles, name=f'{id}')
            await ctx.author.add_roles(role)
            await ctx.send(f'You have succesfully bought the `{role}` role for `{pricerole}`.')
            c.execute('UPDATE balances SET balance = ? WHERE username = ?', (newbalance, author))
            return



    newbalance = balance - price
    price_difference = -newbalance 

    if newbalance < 0:
        await ctx.send(f'You dont have enough money u need `{price_difference }`.')
        return

    


    c.execute('UPDATE balances SET balance = ? WHERE username = ?', (newbalance, author))



            


def idbycharacter():
    c.execute('CREATE TABLE IF NOT EXISTS idbyrole(name TEXT, id INTEGER, price TEXT)')
    for x,y in all_role.items():
        d = random.randint(1000, 9999)
        c.execute(f'INSERT INTO idbyrole(name, id, price) VALUES(?, ?, ?)', (x, d, y,))
        print(f'added {x}, {y} into the table')
        con.commit()

@client.command()
async def setup(ctx):
    guild = ctx.guild 
    for x in all_role.keys():
        await guild.create_role(name=f'{x}')
        await ctx.send(f'created an role with the name {x}')


@client.command()
async def version(ctx):
    message = ctx.message
    author = ctx.message.author
    await ctx.reply('The current version is `1.0`!')
    await message.delete()

@client.command()
async def ping(ctx):
    await ctx.send( "Pong! {} ms".format(int((bot.latency)*(10**3))))

class confirmation_reset_play(nextcord.ui.View):
    @nextcord.ui.button(label='✅ yes ', style=nextcord.ButtonStyle.blurple)
    async def ye(self, button : nextcord.ui.button, interaction: nextcord.Interaction):
        channel = interaction.channel
        author = bot.author
        if interaction.user == author:
            c.execute('SELECT * FROM balances WHERE username = ?', (author,))
            balancefetch = c.fetchone()
            if balancefetch is None:
                balance  = 0
            else:
                balance = balancefetch[1]
                price= 100
            new_balance = balance - price
            difference = price - balance
            if new_balance < 0:
                await channel.send(f'u have {difference} ryo short')
                return
            else:
                c.execute('UPDATE balances SET balance = ? WHERE username = ?', (new_balance, author))
                await channel.send(f'Succesfully reseted the $play cmd for {author}.') 
                c.execute('CREATE TABLE IF NOT EXISTS play(author TEXT, answer TEXT, link TEXT)')
                item1 = random.choice(list(k.values()))
                bot.name = (next((key for key, value in k.items() if value == item1), None))
                y = nextcord.Embed(color=0x000000)
                y.set_image(url=item1)
                y.set_footer(text=f'use $play  to guess it')
                await channel.send(embed = y)
                c.execute('INSERT INTO play(author, answer, link) VALUES(?, ?, ?)', (author, bot.name, item1))
                con.commit()
                await bot.hg.delete()
                button.disabled = True
                return
    @nextcord.ui.button(label='❌ no ', style=nextcord.ButtonStyle.blurple)
    async def yes(self, button : nextcord.ui.button, interaction: nextcord.Interaction):
        channel = interaction.channel
        if interaction.user == bot.author:
            button.disabled = True
            return

@client.command()
async def play(ctx, *, guess = None):
    author = ctx.author.name
    ryo=([30, 40, 50, 60, 70], [40, 20, 10, 7.5, 2.5])
    p=(['D', 'C', 'B', 'A', 'S'], [50, 20, 20, 9.99, 0.001])
    
    con.commit()
    c.execute('SELECT * FROM play WHERE author = ?', (author,))
    guesfetch = c.fetchone()
    if guesfetch is None:
        author = ctx.author.name
        c.execute('CREATE TABLE IF NOT EXISTS play(author TEXT, answer TEXT, link TEXT)')
        item1 = random.choice(list(k.values()))
        bot.name = (next((key for key, value in k.items() if value == item1), None))
        y = nextcord.Embed(color=0x000000)
        y.set_image(url=item1)
        y.set_footer(text=f'Use play `name` to guess it.')
        await ctx.send(embed = y)
        c.execute('INSERT INTO play(author, answer, link) VALUES(?, ?, ?)', (author, bot.name, item1))
        con.commit()
        return
    if guess == 'reset':
        bot.author = author
        bot.hg = await ctx.send('Do you really want to reset it and pay 100 to reset it?', view=confirmation_reset_play())
        return 
    if guess == 'show':
        c.execute('SELECT * FROM play WHERE author = ?', (author,))
        showfetch = c.fetchone()
        if showfetch is None:
            await ctx.send('You cant show the character if u didnt start the game.')
            return
        g = nextcord.Embed(color=0x000000)
        g.set_image(url=showfetch[2])
        await ctx.send(embed = g )
        return
    if guesfetch[1] == guess:
        rank = random.choices(*p)
        c.execute('SELECT * FROM idbycharacter WHERE name = ?', (guess,))
        idfetch = c.fetchone()
        if idfetch == None:
            id = 999999
        else:
            id = idfetch[2]
        await ctx.send(f'You have succesfully claimed {guess}.')
        print(repr(author))
        c.execute('DELETE FROM play WHERE author = ?;', (author,))
        c.execute(f'INSERT INTO claimed_cards(name, rank, id) VALUES(?, ?, ?)', (guesfetch[1], rank, idfetch[2] ))
        con.commit()
        return
    if guesfetch[1] is not guess:
        await ctx.send(f'The guess `{guess}` is not right. ')
        return
    else:
        con.commit
        return


@client.command()
@commands.cooldown(1, 43200, commands.BucketType.user)
@commands.has_any_role("Sharigan",)
async def sharigan(ctx):
    author = ctx.author.name
    price = random.randint(50, 150)
    c.execute('SELECT * FROM balances WHERE username = ?', (author,))
    balancefetch = c.fetchone()
    if balancefetch is None:
        balance  = 0
    else:
        balance = balancefetch[1]
        newbalance = price + balance
    c.execute('UPDATE balances SET balance = ? WHERE username = ?', (newbalance, author))
    await ctx.send(f' u have succesfully used your ability and got `{price}` ryo from that! ')

@client.command()
@commands.cooldown(1, 54000, commands.BucketType.user)
@commands.has_any_role("Sagemode",)
async def sagemode(ctx):

    author = ctx.author.name
    price = random.randint(150, 300)
    c.execute('SELECT * FROM balances WHERE username = ?', (author,))
    balancefetch = c.fetchone()
    if balancefetch is None:
        balance  = 0
    else:
        balance = balancefetch[1]
        newbalance = price + balance
    c.execute('UPDATE balances SET balance = ? WHERE username = ?', (newbalance, author))
    await ctx.send(f' u have succesfully used your ability and got `{price}` ryo from that! ')

@client.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
@commands.has_any_role("Izanami",)
async def izanami(ctx):
    author = ctx.author.name
    price = random.randint(400, 650)
    c.execute('SELECT * FROM balances WHERE username = ?', (author,))
    balancefetch = c.fetchone()
    if balancefetch is None:
        balance  = 0
    else:
        balance = balancefetch[1]
        newbalance = price + balance
    c.execute('UPDATE balances SET balance = ? WHERE username = ?', (newbalance, author))
    await ctx.send(f' u have succesfully used your ability and got `{price}` ryo from that! ')

@client.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
@commands.has_any_role("Izanagi",)
async def izanagi(ctx):
    author = ctx.author.name
    price = random.randint(400, 650)
    c.execute('SELECT * FROM balances WHERE username = ?', (author,))
    balancefetch = c.fetchone()
    if balancefetch is None:
        balance  = 0
    else:
        balance = balancefetch[1]
        newbalance = price + balance
    c.execute('UPDATE balances SET balance = ? WHERE username = ?', (newbalance, author))
    await ctx.send(f' u have succesfully used your ability and got `{price}` ryo from that! ')

@client.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
@commands.has_any_role("Eightgates",)
async def eightgates(ctx):
    author = ctx.author.name
    price = random.randint(350, 600)
    c.execute('SELECT * FROM balances WHERE username = ?', (author,))
    balancefetch = c.fetchone()
    if balancefetch is None:
        balance  = 0
    else:
        balance = balancefetch[1]
        newbalance = price + balance
    c.execute('UPDATE balances SET balance = ? WHERE username = ?', (newbalance, author))
    await ctx.send(f' u have succesfully used your ability and got `{price}` ryo from that! ')

@client.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
@commands.has_any_role('Susanoo',)
async def susanoo(ctx):
    author = ctx.author.name
    price = random.randint(250, 500)
    c.execute('SELECT * FROM balances WHERE username = ?', (author,))
    balancefetch = c.fetchone()
    if balancefetch is None:
        balance  = 0
    else:
        balance = balancefetch[1]
        newbalance = price + balance
    c.execute('UPDATE balances SET balance = ? WHERE username = ?', (newbalance, author))
    await ctx.send(f' u have succesfully used your ability and got `{price}` ryo from that! ')

@client.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
@commands.has_any_role("Tailedbeastbomb",)
async def tailedbeastbomb(ctx):
    author = ctx.author.name
    price = random.randint(250, 450)
    c.execute('SELECT * FROM balances WHERE username = ?', (author,))
    balancefetch = c.fetchone()
    if balancefetch is None:
        balance  = 0
    else:
        balance = balancefetch[1]
        newbalance = price + balance
    c.execute('UPDATE balances SET balance = ? WHERE username = ?', (newbalance, author))
    await ctx.send(f' u have succesfully used your ability and got `{price}` ryo from that! ')

@client.command()
@commands.cooldown(1, 43200, commands.BucketType.user)
@commands.has_any_role("Rasengan",)
async def rasengan(ctx):
    author = ctx.author.name
    price = random.randint(50, 150)
    c.execute('SELECT * FROM balances WHERE username = ?', (author,))
    balancefetch = c.fetchone()
    if balancefetch is None:
        balance  = 0
    else:
        balance = balancefetch[1]
        newbalance = price + balance
    c.execute('UPDATE balances SET balance = ? WHERE username = ?', (newbalance, author))
    await ctx.send(f' u have succesfully used your ability and got `{price}` ryo from that! ')

@client.command()
@commands.cooldown(1, 43200, commands.BucketType.user)
@commands.has_any_role("Amaterasu",)
async def amaterasu(ctx):
    author = ctx.author.name
    price = random.randint(75, 175)
    c.execute('SELECT * FROM balances WHERE username = ?', (author,))
    balancefetch = c.fetchone()
    if balancefetch is None:
        balance  = 0
    else:
        balance = balancefetch[1]
        newbalance = price + balance
    c.execute('UPDATE balances SET balance = ? WHERE username = ?', (newbalance, author))
    await ctx.send(f' u have succesfully used your ability and got `{price}` ryo from that! ')

@client.command()
@commands.cooldown(1, 43200, commands.BucketType.user)
@commands.has_any_role("chibakutensei",)
async def chibakutensei(ctx):
    author = ctx.author.name
    price = random.randint(75, 175)
    c.execute('SELECT * FROM balances WHERE username = ?', (author,))
    balancefetch = c.fetchone()
    if balancefetch is None:
        balance  = 0
    else:
        balance = balancefetch[1]
        newbalance = price + balance
    c.execute('UPDATE balances SET balance = ? WHERE username = ?', (newbalance, author))
    await ctx.send(f' u have succesfully used your ability and got `{price}` ryo from that! ')

@client.command()
@commands.cooldown(1, 43200, commands.BucketType.user)
@commands.has_any_role("Chidori",)
async def chidori(ctx):
    author = ctx.author.name
    price = random.randint(50, 150)
    c.execute('SELECT * FROM balances WHERE username = ?', (author,))
    balancefetch = c.fetchone()
    if balancefetch is None:
        balance  = 0
    else:
        balance = balancefetch[1]
        newbalance = price + balance
    c.execute('UPDATE balances SET balance = ? WHERE username = ?', (newbalance, author))
    await ctx.send(f' u have succesfully used your ability and got `{price}` ryo from that! ')


@client.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
@commands.has_any_role("Spop",)
async def spop(ctx):
    author = ctx.author.name
    price = random.randint(350, 650)
    c.execute('SELECT * FROM balances WHERE username = ?', (author,))
    balancefetch = c.fetchone()
    if balancefetch is None:
        balance  = 0
    else:
        balance = balancefetch[1]
        newbalance = price + balance
    c.execute('UPDATE balances SET balance = ? WHERE username = ?', (newbalance, author))
    await ctx.send(f' u have succesfully used your ability and got `{price}` ryo from that! ')

@client.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
@commands.has_any_role("Tsukuyomi",)
async def tsukuyomi(ctx):
    author = ctx.author.name
    price = random.randint(250, 450)
    c.execute('SELECT * FROM balances WHERE username = ?', (author,))
    balancefetch = c.fetchone()
    if balancefetch is None:
        balance  = 0
    else:
        balance = balancefetch[1]
        newbalance = price + balance
    c.execute('UPDATE balances SET balance = ? WHERE username = ?', (newbalance, author))
    await ctx.send(f' u have succesfully used your ability and got `{price}` ryo from that! ')


@client.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
@commands.has_any_role("Rinnegan",)
async def rinnegan(ctx):
    author = ctx.author.name
    price = random.randint(250, 450)
    c.execute('SELECT * FROM balances WHERE username = ?', (author,))
    balancefetch = c.fetchone()
    if balancefetch is None:
        balance  = 0
    else:
        balance = balancefetch[1]
        newbalance = price + balance
    c.execute('UPDATE balances SET balance = ? WHERE username = ?', (newbalance, author))
    await ctx.send(f' u have succesfully used your ability and got `{price}` ryo from that! ')

@client.command()
@commands.cooldown(1, 86400, commands.BucketType.user)
@commands.has_any_role("Summon",)
async def summon(ctx):
    author = ctx.author.name
    price = random.randint(300, 550)
    c.execute('SELECT * FROM balances WHERE username = ?', (author,))
    balancefetch = c.fetchone()
    if balancefetch is None:
        balance  = 0
    else:
        balance = balancefetch[1]
        newbalance = price + balance
    c.execute('UPDATE balances SET balance = ? WHERE username = ?', (newbalance, author))
    await ctx.send(f'u have succesfully used your ability and got `{price}` ryo from that! ')


@client.command(aliases=['Clear'])
@commands.has_permissions(manage_messages=True)
async def clear(ctx, *, amount=5):
    now = datetime.now()
    author = ctx.author
    dt_string = now.strftime("%H:%M:%S")
    await ctx.channel.purge(limit=amount)
    print(f'[{dt_string} clearing messages]')
    await ctx.send(f"er zijn {amount} messages gecleared")
    if amount == 1: 
        print(f'[{dt_string}] {author} heeft {amount} message gecleared')
        return
    else:
        print(f'[{dt_string}] {author} heeft {amount} messages gecleared')
        return





@client.command()
async def teleport(ctx, *, place= None):
    author = ctx.author.name
    c.execute('CREATE TABLE IF NOT EXISTS teleportplaces(place TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS teleport(author TEXT, place TEXT)')
    c.execute('SELECT * FROM teleportplaces')
    print(c.fetchall())
    place =['ramen shop', '4th great ninja war', 'hokage\'s office', 'hashirama madara statue', 'nakano shrine', 'land of fire', 'land of water', 'land of rain', 'land of clouds', 'land of mist']
    tpplace = random.choice(place)
    price = random.randint(75, 150 )
    c.execute('SELECT * FROM balances WHERE username = ?', (author,))
    balinfo = c.fetchone()
    if balinfo is None:
        balance = 0
    else:
        balance = balinfo[1]
    newbalance = balance + price
    c.execute('UPDATE balances SET balance = ? WHERE username = ?', (newbalance, author))
    await ctx.send(f'u have succesfully teleported to `{tpplace}` and gained `{price}`.')
    con.commit()



@client.command()
async def bugreport(ctx, *, report=None):
    if report is None:
        await ctx.send('Make sure to put in a report! ')
        return
    user = client.get_user(786150856792735745)
    em = nextcord.Embed(title=f'bug report from {ctx.author}', description=f'{report}')
    await user.send(embed= em)
    await ctx.send('Succesfully sended the bugreport to the owner of the bot!')




@client.command()
async def help(ctx, *, help='general'):
    if help == "general":
        general = nextcord.Embed(color=0x000000, title='general help command for Sensei 📂', description='\u200b')
        general.add_field(name='$version ⤴️', value='Lets you see the current version of the bot. \n ')
        general.add_field(name='$bugreport 🐛  ', value='If you have any issues with the bot or it stops working use this command and a developer will get into it as soon as possible! \n ')
        general.add_field(name='\u200b', value='\u200b')
        general.add_field(name='$ping 🏓', value='lets you see the latency time \n from you to the bot \n \u200b' )
        general.add_field(name='$tutorial 📺', value='shows a tutorial with content \n going over the claim command.\n ',)
        general.add_field(name='\u200b', value='\u200b')
        general.add_field(name='$shop', value='shows what you can buy! 🙃',)
        await ctx.send(embed=general)

keep_alive()
client.run('TOKEN')