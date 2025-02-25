import streamlit as st

st.set_page_config(page_title='Mindset Growth',page_icon='🌱')



st.title('\U0001f600 Growth Mindset Challenge: Web App with Streamlit')
st.header('🧠 Welcome to the Mindset Growth Project')
st.write('A growth mindset fosters resilience, adaptability, and a love for lifelong learning, helping individuals achieve personal and professional success.🌟🤩')


st.header("⚡ Today's Growth Mindset Quotes!")
st.write('**Do not be embarrassed by your failures, learn from them and start again** – Richard Branson')


st.header("🏆 What's your today challange")
user_input =  st.text_input('*Enter your challange today you are facing*')

# condition
if user_input :
    st.success(f'Oh Your facing this problem **{user_input}**. Keep pushing toward your goal your facing !')
else :
    st.warning('Tell us about your goal!')


st.header('Relection on Your Goal')
reflection = st.text_area('Write what you think?')

# reflecting
if reflection:
    st.success(f'Great **{reflection}**')
else :
    st.info('Reflecting on past experience help you grow!. Share your difficulties')


# acheivement 
st.header('Celebrate Your wins🏆')
acheivement=  st.text_input('Share your are recently accomplished:')

if acheivement:
    st.success(f"Great! Your are achieved **{acheivement}**")
else:
    st.info('Share your achievement now 🤩')

# footer
st.write('-------------------------------------------------------------------------')
st.write('\nKeep learning and believing in yourself')
st.write('\nCreated by Qirat Saeed')