# N8N Projects

This repository contains a Streamlit-based personal assistant app connected to an n8n workflow through a webhook.
<img width="1643" height="872" alt="image" src="https://github.com/user-attachments/assets/7c9156a6-3186-4503-a914-95ca58e7fea5" />


## Files

- `app.py` - Streamlit chat interface
- `test_webhook.py` - simple webhook test script
- `main.py` - minimal Python entry file

## Features

- Chat-style Streamlit interface
- Sends user prompts to an n8n webhook
- Supports JSON and plain-text webhook responses
- Improved error handling for invalid webhook replies

## Requirements

- Python 3.10+
- `streamlit`
- `requests`
- A running local n8n instance

Install dependencies:

```bash
pip install streamlit requests
```

## Run The App

Start the Streamlit app with:

```bash
streamlit run app.py
```

## n8n Setup

Make sure your n8n workflow:

- is running on `http://localhost:5678`
- uses the webhook URL configured in `app.py`
- is active if you are using a production webhook URL
- returns a response back to Streamlit

If you use a test webhook:

```text
/webhook-test/...
```

click `Listen for test event` in n8n before sending the request.

If you use a production webhook:

```text
/webhook/...
```

activate the workflow first.

## Author

Created by Adity Pujari.
