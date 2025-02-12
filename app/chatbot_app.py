import streamlit as st

# Title of the app
st.title("Simple Chatbot UI")

# Initialize session state for chat history
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Function to generate a simple response
def generate_response(user_input):
    # Simple echo bot
    return f"Echo: {user_input}"

# User input
user_input = st.text_input("You:", key="user_input")

# Button to send message
if st.button("Send"):
    if user_input:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": user_input})
        # Generate and add bot response to chat history
        response = generate_response(user_input)
        st.session_state.messages.append({"role": "bot", "content": response})

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"**You:** {message['content']}")
    else:
        st.markdown(f"**Bot:** {message['content']}")
