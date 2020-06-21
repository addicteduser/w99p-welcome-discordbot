import os
import discord
from discord.ext import commands
from discord.utils import get

# for local development
# from secrets import DISCORD_TOKEN
# token = DISCORD_TOKEN

# for deployment
token = os.environ['DISCORD_TOKEN']


bot = commands.Bot(command_prefix=commands.when_mentioned,
                   case_insensitive=True,
                   description='Waterdeep 99th Precinct server\'s personal welcome bot.',
                   help_command=None)

#######################
## DISCORD BOT START ##
#######################


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

    print('Connected to the following Discord servers: ')
    for guild in bot.guilds:
        print(f' >> {guild.name}')

#########################
## DISCORD BOT LOGGING ##
#########################


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CommandError):
        await ctx.send(f'Oof! Sorry, {ctx.author.mention}. I\'m just the welcoming committee. Maybe you can consult someone else.')

    # log_error(error, ctx.message.content)


# def log_error(error, msg):
#     print(f'ERROR: {error}')
#     print(f'COMMAND: {msg}')


@bot.event
async def on_member_join(member):
    channel_lobby = get(member.guild.channels, name="coffee-and-donuts")
    await channel_lobby.send(get_welcome_message(member.guild, [member]))

##################
## BOT COMMANDS ##
##################


@bot.command()
async def greet(ctx, members: commands.Greedy[discord.Member] = None, *args):
    await ctx.send(get_welcome_message(ctx.guild, members))


def mention_channel(guild, channel_name):
    return get(guild.channels, name=channel_name).mention


def get_welcome_message(guild, members):
    print('here')
    tutor = get(guild.members, name='corgibutt')

    welcome_message = ''

    if members is not None:
        newbies = ", ".join(newb.mention for newb in members)
        welcome_message = f'Hi, {newbies}!\n\n'

    welcome_message = welcome_message + \
        f'Welcome to the server! I am Welcome Wagon, resident semi-sentient Help AI. Let me give you a tour.\n\nStarting from top to bottom:\n\n' + \
        f'- {mention_channel(guild,"change-my-nickname")} and {mention_channel(guild,"use-the-bots")} speak for themselves.\n' + \
        f'- {mention_channel(guild, "get-your-roles")} to show users here if you\'re a DM or player. These roles give your usernames those colors and lets you view the server channels that we use for games.\n\n' + \
        f'- {mention_channel(guild, "ground-rules")} for __**server rules Vault**__.\n' + \
        f'- {mention_channel(guild, "how-to-dnd-5e")} for video __tutorials for learning D&D__.\n' + \
        f'- {mention_channel(guild, "how-to-al")} for the **important documents** for new Adventurers League players and DMs.\n' + \
        f'- {mention_channel(guild, "tutorial-room")} is where you can __ask people your D&D questions__. This is also where {tutor.mention} conducts her 1-on-1 and/or group tutorials.\n\n' + \
        f'- {mention_channel(guild, "coffee-and-donuts")} is the __general lobby__ where you nerds can mingle.\n' + \
        f'- {mention_channel(guild, "test-bots-here")} is where you can __practice using the discord bots__.\n' + \
        f'- {mention_channel(guild, "case-assignments")} is where you can assign roles to yourselves (as per {mention_channel(guild, "get-your-roles")}).\n' + \
        f'- {mention_channel(guild, "title-of-your-sex-tape")} is **NSFW**. View at your own risk. I mean it.\n\n' + \
        f'- {mention_channel(guild, "officer-badge-numbers")} for the listed DMs of this server.\n' + \
        f'- {mention_channel(guild, "lost-and-found-evidence")} for __trading Adventurers League items__.\n' + \
        f'- {mention_channel(guild, "open-case-requests")} for you thirsty adventurers looking to play.\n' + \
        f'- {mention_channel(guild, "open-cases")} for __game schedules__.\n\n' + \
        'That\'s it for now. Thanks for attending the tour!'

    return welcome_message


if __name__ == '__main__':
    bot.run(token)
