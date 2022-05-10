from discord.ext import commands
import random

config = {
    'token': "OTYzNzc2NDc0MDg5OTM5MDA1.YlbAyQ.GNxMM5hCxa9HYOPnXDwkCelf41A",
    'prefix': 'prefix',
}

client = commands.Bot(command_prefix=config['prefix'])


def RandName(li):
    return li[random.randint(0, len(li)-1)]


@client.event
async def on_message(ctx):
    if ctx.author != client.user:
        print(ctx)
        if ctx.content[0] == "~":
            if ctx.content.split()[0] == "~help":
                await ctx.reply("Команды:\n"
                                "~help - Список команд\n"
                                "~img 'текст' - картинка\n"
                                "~rand-name 'имена через пробел' - рандомный человек\n"
                                "\n")

            if ctx.content.split()[0] == "~rand-name":
                if len(ctx.content.split()) > 1:
                    n = []
                    for i in ctx.content.split():
                        if i != "~rand-name":
                            n.append(i)
                    await ctx.reply(f"```md\n{RandName(n)}```")
                else:
                    await ctx.reply("```diff\n-ОШИБКА: Введите имена```")



client.run(config['token'])
