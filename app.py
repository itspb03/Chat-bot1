# longwall_mining_chatbot.py
# Author: Pranay Bhaskar
import streamlit as st

# Knowledge Base with keywords
knowledge_base = {
    "longwall mining": "Longwall mining is an underground coal mining method where a long wall of coal is mined in a single slice, typically 0.6–1.0 m thick.",
    "how it works": "It uses a mechanized shearer that moves back and forth across a coal face. Hydraulic roof supports hold up the roof temporarily while coal is removed, and the roof is allowed to collapse behind the operation (called 'goaf').",
    "equipment": "Key equipment includes the shearer, armored face conveyor (AFC), hydraulic roof supports, stage loader, and belt conveyor system.",
    "advantages": "High production rates, efficient coal recovery (up to 80%), and relatively low labor requirement compared to other underground mining methods.",
    "disadvantages": "High upfront capital cost, less flexible for varying seam thickness, and can cause significant subsidence above ground.",
    "safety": "Regular equipment inspections, dust suppression systems, methane monitoring, ventilation, and proper roof control plans.",
    "goaf": "The goaf is the collapsed area behind the roof supports after coal extraction in longwall mining."
}

# Function to find best matching response
def get_response(user_query):
    user_query = user_query.lower()
    for keyword, answer in knowledge_base.items():
        if keyword in user_query:
            return answer
    return "I’m not sure about that. Could you rephrase or ask about longwall mining specifically?"

# Streamlit UI
st.set_page_config(page_title="Longwall Mining Chatbot", page_icon="⛏️", layout="centered")

st.title("🤖 Longwall Mining Chatbot")
st.write("Ask me about **Longwall Mining**. Type a question below 👇")

# Store chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input box
user_input = st.text_input("You:", "")

if user_input:
    if user_input.lower().strip() == "quit":
        st.session_state.chat_history.append(("Bot", "Goodbye! Stay safe underground. ⛏️"))
    else:
        response = get_response(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", response))

# Display chat history
for speaker, message in st.session_state.chat_history:
    if speaker == "You":
        st.markdown(f"**{speaker}:** {message}")
    else:
        st.markdown(f"<span style='color:green'>**{speaker}:** {message}</span>", unsafe_allow_html=True)
