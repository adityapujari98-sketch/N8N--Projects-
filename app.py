import streamlit as st
import requests


def extract_ai_response(payload):
    """Handle common n8n webhook response shapes safely."""
    if isinstance(payload, list) and payload:
        first_item = payload[0]
        if isinstance(first_item, dict):
            return first_item.get("output") or first_item.get("message") or str(first_item)
        return str(first_item)

    if isinstance(payload, dict):
        return (
            payload.get("output")
            or payload.get("message")
            or payload.get("response")
            or payload.get("text")
        )

    return None

# create the title for the page
st.title("🤝 Your Personal Assistant")

# add subheader
st.subheader("What can your personal assistant do?")

# create a list of what your assistant can do
st.markdown("""
            1. Answer questions on various topics.   
            2. Arrange Calendar events and meetings.  
            3. Read your emails and send replies, can even summarize them for you.
            4. Manage your tasks and to-do lists.
            5. Take quick notes for you.
            6. Track your expenses and budgeting.
            """)

# add chats subheader
st.subheader("💬 Chat with your assistant")

# create a session state for message history
if "messages" not in st.session_state:
    st.session_state.messages = []

# show the messages in chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# create a chat input box
user_message = st.chat_input()

      
# if user sends a message
if user_message:
    with st.chat_message("user"):
        st.markdown(user_message)
        # append the user message to message history
        st.session_state.messages.append({"role": "user", "content": user_message})
    
    # send the user message to the n8n webhook
    response = requests.post(
        "http://localhost:5678/webhook/c164777d-0a85-4d20-851c-096a24791b46",  # replace with your n8n webhook URL
        json={"message": user_message}
    )
    
    try:
        response.raise_for_status()
        try:
            payload = response.json()
            ai_response = extract_ai_response(payload)

            if not ai_response:
                ai_response = f"Webhook returned an unexpected response: {payload}"
        except ValueError:
            # Some n8n flows answer with plain text instead of JSON.
            ai_response = response.text.strip() or "Webhook returned an empty response."
    except requests.RequestException as exc:
        ai_response = f"Webhook request failed: {exc}"
    
    # display the AI response in chat
    with st.chat_message("assistant"):
        st.markdown(ai_response)
        # append the AI response to message history
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
