# N8N Projects

This repository contains two practical projects built around automation, frontend dashboards, and AI-assisted workflows:

- A solar ROI and system-sizing dashboard for Germany in `index.html`
- A Streamlit chat assistant in `app.py` connected to an n8n webhook

## Project Structure

- `index.html` - interactive solar calculator dashboard with live data cards
- `app.py` - Streamlit chat UI that sends user prompts to an n8n webhook
- `test_webhook.py` - quick script for testing webhook responses outside Streamlit
- `main.py` - minimal Python entry file

## Features

### Solar Dashboard

- Solar system sizing and ROI estimation
- Germany-focused electricity rate and feed-in assumptions
- Live context cards for:
  - Atmospheric CO2
  - Solar irradiance
  - Berlin AQI feed
  - German grid CO2 intensity
- Responsive single-file frontend

### Streamlit Personal Assistant

- Chat-style Streamlit interface
- Sends prompts to an n8n webhook
- Supports webhook responses returned as JSON or plain text
- Safer response parsing and better webhook error handling

## Requirements

### For the dashboard

- Any modern browser

### For the Streamlit app

- Python 3.10+
- `streamlit`
- `requests`
- A running local n8n instance

Install Python dependencies with:

```bash
pip install streamlit requests
```

## Running the Projects

### 1. Solar dashboard

Open `index.html` directly in your browser.

### 2. Streamlit assistant

Run:

```bash
streamlit run app.py
```

Make sure your n8n workflow is:

- running locally on `http://localhost:5678`
- using the same webhook URL configured in `app.py`
- active if you are calling the production webhook URL
- returning a response through a `Respond to Webhook` node when needed

## n8n Notes

If you use the production webhook path:

```text
/webhook/...
```

the workflow must be active.

If you use the test webhook path:

```text
/webhook-test/...
```

you need to click `Listen for test event` in n8n before sending a request.

## Current Improvements

- Better webhook response parsing in the Streamlit app
- Clearer fallback handling for invalid or empty webhook responses
- Stronger live-data sanity checks in the dashboard
- More accurate AQI status messaging for the Berlin feed

## Future Ideas

- Add environment variable support for webhook URLs and API keys
- Split the dashboard JavaScript into reusable modules
- Add screenshots and deployment instructions
- Add tests for webhook payload shapes

## Author

Created by Adity Pujari.
