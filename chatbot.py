from nltk.chat.util import Chat, reflections
import datetime

pairs = [
         ['my name is (.*)' ,['hii %1']],
    ['hello|hey|hellu|holla|hii' ,['hey there','hii there','haayy']],
    ['(.*) in (.*) is fun',['%1 in %2 is indeed fun']],
    ['(.*)(location|city) ?',['Patna' ]],
    ['(.*)created you',['kajal did using NLTK']],
    ['(.*) is the weather in (.*)',['the weather in %2 is amazing like always']],
    ['do you feel',['may be ,I am not sure']],
    ['how are you doing|how are (.*)',['I am doing great!how are you?']],
    ['I am good|fine|doing well too',['Amazing']],
    ['I am sad|(.*)feeling bored|(.*)feeling bored(.*)',['so sorry , bye']],
    ['(.*)your name|what is your name|name please',['My name is Chatbot,How can I help you']],
    ['help|(.*) help (.*)|(.*)help|help(.*)',['I can help You']],
    ['can You sing a song|can you(.*)',['no,i can chat only \U0001F618 ']],
    # ['what time',['%datetime.datetime.now()']],
    ['(.*) ghost(.*)|(.*) ghost|ghost(.*)|ghost',['here are ghosts \U0001F47B  \U0001F47B  \U0001F47B']],
    ['suggest me yummy food|food|(.*)food|food(.*)|(.*)food(.*)',['dosa','Burger','Golgappa','chowmin']],
   
    ['Are You a robot|Are you real',['Yes,I am a robot but i am a smart one']],
    ['tell me something',['i am robot! here to help you']],
    ['Good (.*)',['good %1 ,how can I help']],
    ['happy birthday',['thanks a lot \U0001F600']],
     ['you are (.*)',['thankyou, You are %1 too']],
     ['thank you|thanks|thanku|thankyou',['You\'re welcome \U0001F606']],



     ['bye|bbye|go from here|good bye',['bye,see you soon ','Bbye','tata']],

]
my_dummy_reflections = {
    'go':'gone',
    'hello':'hey there'
}
chat=Chat(pairs,reflections)
# chat._substitute("go hello")
chat.converse()