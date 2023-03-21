# Mandrill Webhooks


This project demonstrates how to process Mandrill email webhooks and update a frontend in real-time using WebSockets.

## Requirements
* Python 3.10
* Django
* Channels
* Channels-Redis
* Daphne
* Redis

## Installation

**Clone this repository:**
```bash
git clone https://github.com/shafikshaon/mandrill-webhooks.git
cd mandrill-webhooks

docker-compose down
docker-compose up
```

## Usage
1. Access the application on `http://localhost:8000` or `http://127.0.0.1:8000`.
2. Configure Mandrill to send webhook events to the application's `/webhook/` endpoint.
3. Watch the frontend update in real-time as Mandrill events are received and processed by the backend.

## Thought process behind the design and implementation of this project

1. **Identify the problem:** The main goal of the project is to process webhook events from Mandrill (such as email opens, clicks, etc.) and update a user interface in real-time using WebSockets.
2. **Choose appropriate technologies:** Since the project is based on Django, we decided to use Django Channels for WebSocket support, Daphne as the ASGI server, and Redis as the backend for message passing.
3. **Design the Django application:** The Django app should have a view to handle incoming webhook events from Mandrill. We create a dedicated Webhook view to process the POST requests containing the webhook payload.
4. **Process webhook events:** When a webhook event is received, the payload is stored in Redis using the Mandrill message ID as the key. This storage allows for easy retrieval and processing of the events later if needed.
5. **Implement WebSocket communication:** Using Django Channels, we create a WebSocket consumer that listens for incoming connections from the frontend. When a new event is received from Mandrill, the backend sends a notification via the WebSocket to the connected frontend clients.
6. **Create a simple frontend:** The frontend consists of an index.html file with JavaScript code to establish a WebSocket connection to the backend. The frontend listens for incoming messages from the WebSocket and updates the user interface accordingly.
7. **Configure the development environment:** The project uses Docker and Docker Compose to create an isolated environment for the Django app, Daphne server, and Redis service. This setup simplifies deployment and ensures consistency across different platforms.
8. **Test the application:** The application is tested by sending sample webhook events from Mandrill and observing the frontend updates in real-time. Additionally, unit tests can be written for the Django views and WebSocket consumer to ensure their proper functioning.
9. **Document the project:** A README.md file is created to provide an overview of the project, installation instructions, usage guidelines, and other relevant information.
