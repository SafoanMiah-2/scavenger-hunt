import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title='Memory Scavenger Hunt', page_icon='📌', layout="centered", initial_sidebar_state="collapsed", menu_items=None)

st.markdown('# SCAVENGER HUNT')
st.markdown('Only with the right answer will the path forward be revealed.')
st.markdown('---')



page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://i.postimg.cc/4xgNnkfX/Untitled-design.png");
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""



st.markdown(page_bg_img, unsafe_allow_html=True)

def check(variable, answer):
    if variable != answer:
        st.stop()


# section 1
first = st.date_input('On a day when the stars first aligned for us, a new chapter began. It was a day marked by the spark of our first hello. Uncover the date of that fateful meeting, and you’ll find the next clue in our story. ✨📅')
check(str(first), '2023-11-22')
st.markdown('---')
#2023-11-22


# section 2
song = st.text_input('In the midst of festive cheer, you presented a gift that whispered a familiar tune. It was a melody embedded in our hearts and playlist, encased in a charming keepsake. To find the next clue, unravel the song that played a sweet serenade during our Christmas. Hint: Spotify. P.S: check your spelling! 🎁🎵')
check(song.lower(), "can't help falling in love")
st.markdown('---')
#can't help falling in love


# section 3
chirstmas_movie = st.text_input('✨ Let’s travel back to the dawn of our shared story. Seek out the first **social public** tribute I made to your culinary brilliance. Within the comments of this initial homage, a subtle hint awaits to lead you to the next chapter. 📸🍴🌟')
check(chirstmas_movie.lower(), 'klaus')
st.image('img/klaus.png')
st.markdown('---')
#klaus


# section 4
email = st.text_input('safxriley@protonmail . com | AH88#THfytX9$corㅤ|ㅤ✉️')
check(email.upper(), 'MDWRVQKZPVBXNSNHZFVXMEXPPRGSCNXMOOKZLORUPQZJTHCQABTCTQLIQHJBRRAXRSUGJMGUGEBATGEUOZRILNWQHDIZRGLNIECZWIOEDUTUQVOVTSRZTRMHQNNGOOINDKRQJANNVIXQEOKFPQQFEQAVEJBWNFNAJAMFXSEYOVAVAIYAGDAWVLZKEBQMWUFEECQCLTANVLLBCZCCWUOZCOSQOUOKSUBQNXYUEBOPVEKYRELMBHOLIBDGOOUULWQUNUZJHGIXMVECQRHYKDJDQFSGAXKEGVENNYJSCSFCUMIKASUCZBYRXVEHRBLWBPNFTCMIJNDOJZRETGGREZYALAIHVWTWFQVWNLLIMNXOHMUQGRWGDIYPYTERFIVAMKOOXJSYLFJVEQBONVTLCVPWMUCRDBNLKXIFHGOIQVVVEUHVUNGXEVHOHHFPMIYLMEWSGUYROPEBHTYGESOJAODGEPLXDPEZSYDWPUYQDJJZJLFPBZJHHTWPUOHDJOMPHIEVIMRMLMOCNPJHWGWEQLNBRBACMBHTFXXRIICLYYEBSCYGLIRHALMMUAKYDOAPNAWBRMFXEKDPGVBRUQRYFCGMJNZG')
st.markdown('''These **letters** might prove essential down the line.''')
st.markdown('---')


# section 5 (number 10)
password = st.text_input("Amidst the digital landscape where we keep our cherished files, a new clue awaits your discovery. This familiar blue box in the cloud holds the next piece of our puzzle. When you're ready, log in and delve into this secure space where our secrets are safeguarded. 📦☁️💙")
check(password.lower(), 'i love you 3000')
col1, col2 = st.columns(2)
col1.markdown('The missing 19th piece.')
col2.image('img/19.png')
st.markdown('---')

number = st.number_input('Our next adventure lies in a blocky world, filled with endless possibilities. One that we’ve spent time building together, from the ground up. Here’s a little piece of that world—an image that holds something special. Look closely; you’ll need to count carefully to find the magic number. 🌷❤️🔢')
check(number, 10)
st.image('img/mc.png')
st.markdown('This **number** will be crucial when the time is right. Keep it close; you’ll need it to unlock steps in your journey.')
st.markdown('---')

# section 7
st.code('''
def build_puzzle(letters, num):

    num *= 2

    print('------------------------- PUZZLE -------------------------')
    print('----------------------------------------------------------')
    cols = len(letters)//num
    rows = len(letters)//cols

    for pos in range(rows):
        print(' '.join(letters[0 + (cols*pos) : cols + (cols*pos)])) 
    
    print('----------------------------------------------------------')


letters = input('LETTERS: ')
num = int(input('NUMBER: '))

build_puzzle(letters, num)
                   ''')

code = st.text_input("To embark on this word search adventure, start by uncovering words that begin with these letters: L, S, S. Each letter is the key to a word you'll find. Running the Python code will guide you to the answer. Ready to dive into the search? 🧩🐍")
check(code.lower(), 'gateway')
st.image('img/gateway.png')
st.markdown('---')

# Section 8
st.audio('img/morse.mp3')
morse = st.text_input('Listen and take note. 🔉📝')
check(morse.lower(), 'ravioli')
st.markdown('---')


# Section 9
cipher = st.text_input('''In the swirling sands of time, the ancient rulers knew the art of shifting letters. Seek their wisdom and unlock the secret hidden within the letters. Only by shifting your perspective will the message become clear. 🗝️🔤''')
st.text("Gsdrsx dro omryoc yp yeb crkbon knfoxdeboc, drobo vsoc k wywoxd grobo gybnc yp kppomdsyx psbcd nkxmon ezyx dro ksb. Drsxu lkmu dy dro nsqsdkv bokvw grobo yeb tyebxoi loqkx, kxn bomkvv dro qkwo sx grsmr droco gybnc gobo czyuox, 'S vyfo iye' 💖💬")
check(cipher.lower(), 'minecraft')
st.image('img/mc2.png', caption='Drsc gsvv mywo sx occoxdskv: ckphbsvoi | KR88#DRpidH9$myb')
st.markdown('---')


# Section 10
st.markdown("In the heart of a past Valentine's surprise, a secret was left waiting. Venture to the digital world and search the mailbox, created just for you. There lies a message among the echoes of love. Seek it out, for it holds the third last piece of our adventure. 🌐🔍💘")

col1, col2, col3 = st.columns(3)

a1 = col1.text_input(' ', key='a1')
a2 = col1.text_input(' ', key='a2')
a3 = col1.text_input(' ', key='a3')
a4 = col1.text_input(' ', key='a4')
a5 = col1.text_input(' ', key='a5')
a6 = col1.text_input(' ', key='a6')

b1 = col2.text_input(' ', key='b1')
b2 = col2.text_input(' ', key='b2')
b3 = col2.text_input(' ', key='b3')
b4 = col2.text_input(' ', key='b4')
b5 = col2.text_input(' ', key='b5')
b6 = col2.text_input(' ', key='b6')

c1 = col3.text_input(' ', key='c1')
c2 = col3.text_input(' ', key='c2')
c3 = col3.text_input(' ', key='c3')
c4 = col3.text_input(' ', key='c4')
c5 = col3.text_input(' ', key='c5')
c6 = col3.text_input(' ', key='c6')

name_values = [
    'Barnette', 'Tux', 'Snowball', 'Kung Pao', 'Pink', 'Appa', 
    'Kiwi', 'Iris', 'Bepper', 'Oatmeal', 'Matcha', 'Girly', 
    'Desmond', 'Purrcy', 'Stripe', 'Barkley', 'Pebble', 'Ravioli'
]
name_inputs = [a1, a2, a3, a4, a5, a6, b1, b2, b3, b4, b5, b6, c1, c2, c3, c4, c5, c6]

#check(name_inputs, name_values)
st.markdown('---')


# Section 11
st.markdown("""
            A new riddle emerges. Embark on a quest to decipher the puzzle hidden in the link below. Within its fragmented pieces lies a cryptic QR code—a key to an elusive video. This video holds the secrets to accessing the next enigmatic realm of our journey. Follow the clues, decode the symbols, and unveil the path that awaits. 🌌🗝️
            **Embark on the quest here:** [Sliding Puzzle](https://puzzel.org/slidingpuzzle/play?p=-O56e-9t3zirMcSadty1)""")
t1 = st.text_input(' ', key='t1')
t2 = st.text_input(' ', key='t2')
t3 = st.text_input(' ', key='t3')
t4 = st.text_input(' ', key='t4')
t5 = st.text_input(' ', key='t5')

button_values = ['oak', 'oak', 'oak', 'jungle', 'warped']
button_inputs = [t1, t2, t3, t4, t5]
button_inputs = [x.lower() for x in button_inputs]
check(button_inputs, button_values)
st.markdown('---')


# Section FINAL
st.markdown('#### Good job on making it thus far, this is the last section 💝')
st.text('Please complete the puzzle before answering the following:')
final_answer = st.text_input('Answer')
final_button = st.button('Complete')

if final_button == True and final_answer.lower() == 'yes':
    st.markdown("Thank you, Riley, I hope you enjoyed this little journey down memory lane. 💝")
    st.snow()
    st.image('img/final.jpg')
else: 
    iframe_html = """
    <iframe style="width: 100%; 
    height: 400px; 
    max-height: 90vh; 
    border-style: solid; 
    border-width: 2px; 
    border-color: #888" allowFullScreen="true" src="https://www.jigsawexplorer.com/online-jigsaw-puzzle-player.html?frm=1&url=aHR0cHM6Ly9pLmliYi5jby9IRm1XVjhTL3dpbGwteW91LWdvLW91dC13aXRoLW1lLmpwZ18obm9fcHJldmlld180KV8obm9wPTEwMCk~&color=plum" title="Jigsaw Puzzle">Jigsaw Puzzle</iframe>
    """
    components.html(iframe_html, height=600)