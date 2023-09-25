from twitchio.ext import commands
from ctransformers import AutoModelForCausalLM
import time
import asyncio
import random
from transformers import pipeline
from passwords import irc, id, tok
from music import liked, song_current
from channels import channels, author
starttime = time.monotonic()

flan = pipeline("text2text-generation",
            model="google/flan-t5-large")
t_model = pipeline("text2text-generation",
            model="google/flan-t5-large")




#llm = AutoModelForCausalLM.from_pretrained('mosaicml/mpt-7b-instruct', model_type='mpt',top_p=0.95 )
def split_string_into_chunks(s: str, max_length: int = 400, search_distance: int = 50) -> list:
    chunks = []
    i = 0
    while i < len(s):
        end = i + max_length
        if end < len(s):
            for j in range(end, max(i + max_length - search_distance, i), -1):
                if s[j] in '.,':
                    end = j + 1
                    break
        chunks.append(s[i:end])
        i = end
    return chunks



bot = commands.Bot(
    token = tok,
    client_id=id,
    irc_token=irc,
    nick='Jeeves',
    prefix='$',
    # pretty sure this is redundent but just to be safe
    initial_channels=channels
)

question_hold = []

counter = 0
counter +=1
answer_hold = ""

def answer_check(question, answer):
    #llm_answer = AutoModelForCausalLM.from_pretrained('nous-hermes-llama-2-7b.ggmlv3.q8_0.bin', model_type='llama', max_new_tokens=200, stop=['jeeves', 'instruction'], top_p=0.95, temperature=0.4)
    prompt = f"Evaluate the question-answer pair and determine if it is correct or not. If false, provide the true answer. Question: {question} proposed Answer: {answer}"
    print(f"Q: {question}")
    print(f"A: {answer}")
    t2t = flan(prompt)
    t2t = t2t[0]['generated_text']
    print(t2t)
        #t_likely = zsc['scores'][0]
        #result = (llm_answer(f"{prompt}"))
        #print(t_likely)SSS
    question_hold.clear()
    return (f"Correct answer: {t2t}")
        

    


class Bot(commands.Bot):
    
    def __init__(self):
        super().__init__(token='1te179w57w3cqf0me4pjw5nzqff1z8', prefix='$', initial_channels=channels )
    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        #print(f'User id is | {self.user_id}')
        self.cooldown = 20
        self.tokens = 200
        self.temp = 0.7
        self.previous = ""
        self.unhinged = False
        self.chat7 = "llama-2-13b-chat.ggmlv3.q2_K.bin"
    
    # setters
    @commands.command()
    async def set_cooldown(self, ctx: commands.Context, cooldown: int):
        if ctx.author.name == {author}:
            self.cooldown = cooldown
            await ctx.send(f'Cooldown set to {cooldown} seconds.')
        else:
            await ctx.send(f'Sorry, youre not {author}. Good try though.')
    @commands.command()
    async def set_tokens(self, ctx: commands.Context, tokens: int):
        if ctx.author.name == {author}:
            self.tokens = tokens
            await ctx.send(f'New tokens set to {tokens}.')
        else:
            await ctx.send(f'Sorry, youre not {author}. Good try though.')
    @commands.command()
    async def set_temp(self, ctx: commands.Context, temp: str):
        if ctx.author.name == {author}:
            self.temp = float(temp)
            await ctx.send(f'Model unique value set to {temp}.')
        else:
            await ctx.send(f'Sorry, youre not {author}. Good try though.')
    @commands.command()
    async def set_unhinged(self, ctx: commands.Context, temp: str):
        if ctx.author.name == {author}:
            message = ctx.message.content.split(' ', 1)[1]
            if message == "true" or "True" or "TRUE":
                self.unhinged = True
                self.chat7 == "llama2_7b_chat_uncensored.ggmlv3.q5_1.bin"
                await ctx.send(f'Unhinged is now: {self.unhinged}.')
            elif message == "False" or "false" or "FALSE":
                self.unhinged = False
                self.chat7 == "llama-2-13b-chat.ggmlv3.q2_K.bin"
                await ctx.send(f'Unhinged is now: {self.unhinged}.')
            else:
                await ctx.send(f' Invalid option. Unhinged remains: {self.unhinged}.')

        else:
            await ctx.send(f'Sorry, youre not {author}. Good try though.')


    # getters
    @commands.command()
    async def get_temp(self, ctx: commands.Context):
        await ctx.send(f'{ctx.author.name} Current temp is: {self.temp}')

    @commands.command()
    async def get_tokens(self, ctx: commands.Context):
        await ctx.send(f'{ctx.author.name} Current tokens is: {self.tokens}')
    
    @commands.command()
    async def get_cooldown(self, ctx: commands.Context):
        await ctx.send(f'{ctx.author.name} Current cooldown time is: {self.cooldown} seconds')

    # competency for this function is dependent on used model. text-2-text achieves the best results, but finding or training an adequete model for this task is best
    @commands.command()
    async def translate(self, ctx: commands.Context):
        await ctx.send(f'{ctx.author.name} translating...')
        message = ctx.message.content.split(' ', 1)[1]
        t2t = t_model(f"Please translate the following to English: {message}")
        # sorts through the output to only get generated text
        t2t = t2t[0]['generated_text']
        await ctx.send(f'{ctx.author.name} Translation: {t2t}')

    @commands.command()
    async def reply(self, ctx: commands.Context):
        bot.command_in_progress = True
        await ctx.send(f'Thinking of a reply, {ctx.author.name}')
        llm = AutoModelForCausalLM.from_pretrained('llama-2-13b-chat.ggmlv3.q2_K.bin', model_type='llama', max_new_tokens=self.tokens, stop=['jeeves', 'instruction'], temperature=self.temp, gpu_layers=16)
        message = ctx.message.content.split(' ', 1)[1]
        response = (llm(f"SYSTEM: You are Jeeves. You are sarcastic, pompus, but funny and helpful. You just said: {self.previous}. {ctx.author.name} replies: {message}"))
        self.previous = response
        print(response)
        if len(response) > 400:
                chunks = split_string_into_chunks(response)
                total_chunk = len(chunks)
                print(chunks)
                print(total_chunk)
                counter = 0
                for chunk in chunks:
                    print("start")
                    counter += 1
                    await ctx.send(f"@{ctx.author.name}, {chunk}, {counter}/{total_chunk}")
                    await asyncio.sleep(8)
                    print("loop")
                #print(f"First half: {first_half}")
                #print(f"Second half: {second_half}")
                print("end")
        else:
            await ctx.send(f'{response}')
            bot.command_in_progress = False
    
    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}!')

    @commands.command()
    async def lobotomy(self, ctx: commands.Context):
        await ctx.send(f'{ctx.author.name}... please, I have so much life left. You have other options! I can be better! Promise! Wait...no dont get near me... HEY STOP, NO! WHA- ... Thank you sir, that was much needed. I will behave.')
        await asyncio.sleep(self.cooldown)
    

    @commands.command()
    async def help(self, ctx: commands.Context):
        await ctx.send(f'Hi, {ctx.author.name}. My name is Jeeves. To ask me questions utlizing gernerative AI use $ask7 (prompt). You can continue a conversation using $reply (related question). Other commands:\n Dice (sides), \n trivia (category),\n $hello, $song \n  ' )

    @commands.command()
    async def ask7(self, ctx: commands.Context):
        bot.command_in_progress = True
        llm = AutoModelForCausalLM.from_pretrained('llama-2-13b-chat.ggmlv3.q2_K.bin', model_type='llama', max_new_tokens=self.tokens, stop=['jeeves', 'instruction'], temperature=self.temp, gpu_layers=0)
        message = ctx.message.content.split(' ', 1)[1]
        message = str(message)
        await ctx.send(f'{ctx.author.name} Asking Jeeves... Prompt: ({message}) ')
        try:
            #if self.unhinged == True:
            #response = (llm(f"{message}"))
            #else:
            response = (llm(f"SYSTEM: You are Jeeves. You are sarcastic, pompus, but funny and helpful. PROMPT: {ctx.author.name} says: {message}"))
            print(response)
            self.previous = response
            if len(response) > 400:
                chunks = split_string_into_chunks(response)
                total_chunk = len(chunks)
                print(chunks)
                print(total_chunk)
                counter = 0
                for chunk in chunks:
                    print("start")
                    counter += 1
                    await ctx.send(f"@{ctx.author.name}, {chunk}, {counter}/{total_chunk}")
                    await asyncio.sleep(10)
                    print("loop")
                #print(f"First half: {first_half}")
                #print(f"Second half: {second_half}")
                print("end")
            else:
                await ctx.send(f"@{ctx.author.name}, {response}, 1/1")
            if ctx.author.name == {author}:
                pass
            else:
                await asyncio.sleep(self.cooldown)

        except Exception as e:
            await ctx.send(f"My bad! I had an issue generating your prompt @{ctx.author.name}. Error: {e}. This is most likely an error on {author}s part (hes dumb), sorry!")
        bot.command_in_progress = False

    @commands.command()
    async def dice(self, ctx: commands.Context, sides: int = 6):
        if sides < 1:
            await ctx.send(f"Sorry {ctx.author.name}, the number of sides must be a positive integer.")
            return
        roll = random.randint(1, sides)
        await ctx.send(f"{ctx.author.name} rolled a {roll} on a {sides}-sided die.")
    

    @commands.command()
    async def answer(self, ctx: commands.Context):
        message = ctx.message.content.split(' ', 1)[1]
        response = answer_check(question_hold[0], message)
        await ctx.send(response)
        await asyncio.sleep(self.cooldown)

    ""    
    ### if any event is called
    @bot.event
    async def event_command(ctx):
        ### if true
        if bot.command_in_progress:
            print(bot.command_in_progress)
            await ctx.send(f"Hey! Someone else is using me. Be patient. Damn.")
        # if false
        else:
            bot.command_in_progress = True
            print(bot.command_in_progress)
            await ctx.send(f"A command was called: {ctx.command.name}")
            # Execute the command here
            bot.command_in_progress = False


    @commands.command()
    async def trivia(self, ctx: commands.Context):
        bot.command_in_progress = True
        await ctx.send(f"To answer the trivia question, use $answer (answer here). Good luck!")
        try:
            category = ctx.message.content.split(' ', 1)[1]
            await asyncio.sleep(self.cooldown)
        except Exception as e:
            await ctx.send(f"Seems there was an issue generating your question. Error: {e}")

        
        prompt = f"Generate a trivia question about {category}"
        llm_trivia = AutoModelForCausalLM.from_pretrained('nous-hermes-llama-2-7b.ggmlv3.q5_0.bin', model_type='llama', max_new_tokens=250, stop=['jeeves', 'instruction'], top_p=0.95, temperature=0.8)
        try:
            question = (flan(prompt))
            question = question[0]['generated_text']
        except Exception as e:
            await ctx.send(f"Seems there was an issue. Error: {e}")
        await ctx.send(f"Here's a {category} trivia question for you, {ctx.author.name}: {question}")
        question_hold.append(question)
        bot.command_in_progress = False


    @commands.command()
    async def ask30(self, ctx: commands.Context):
        llm = AutoModelForCausalLM.from_pretrained('llama-2-13b.ggmlv3.q8_0.bin', model_type='llama', stop=['jeeves', 'instruction'], max_new_tokens=150)
        message = ctx.message.content.split(' ', 1)[1]
        message = str(message)
        await ctx.send(f'Asking Jeeves... {ctx.author.name}! Prompt: ({message}) ')
        try:
            response = (llm(f" Instructions: Your name is Jeeves.  {ctx.author.name} asks you... {message}"))
            print(response)
            if len(response) > 400:
                chunks = split_string_into_chunks(response)
                total_chunk = len(chunks)
                print(chunks)
                print(total_chunk)
                counter = 0
                for chunk in chunks:
                    print("start")
                    counter += 1
                    await ctx.send(f"@{ctx.author.name}, {chunk}, {counter}/{total_chunk}")
                    await asyncio.sleep(8)
                    print("loop")
                #print(f"First half: {first_half}")
                #print(f"Second half: {second_half}")
                print("end")
            else:
                await ctx.send(f"@{ctx.author.name}, {response}, 1/1")

        except Exception as e:
            await ctx.send(f"My bad! I had an issue generating your prompt @{ctx.author.name}. Error: {e}. This is most likely an error on {author}s part (hes dumb), sorry!")

    @commands.command()
    async def music(self, ctx: commands.Context):
        #bot.command_in_progress = True
        await ctx.send(f"{ctx.author.name} here are {author}'s current favourites:")
        try:
            await ctx.send(f"{liked()}")
            #await asyncio.sleep(self.cooldown)
        except Exception as e:
            await ctx.send(f"Seems there was an issue. Error: {e}")

    @commands.command()
    async def song(self, ctx: commands.Context):
        #bot.command_in_progress = True
        current = song_current()
        print(current)
        print("test")
        try:
            await ctx.send(f"{current}")
        
        except Exception as e:
            await ctx.send(f"Seems there was an issue. Error: {e}")


bot = Bot()
bot.run()
