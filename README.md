# Ethics and Integrity FAQ Bot
<p align="center">
  <img src="front_end/bot_vue/src/assets/init.png" alt="Alt Text">
</p>


This is a project that combines a Vue.js frontend with a Python Flask backend to create an interactive ethics and integrity chatbot.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies](#technologies)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This bot provides an interactive chat experience with Bota, a chatbot designed to assist users and answer inquiries on Ethics and Integrity.

## Features

- Real-time chat interface
- Vue.js frontend for a seamless user experience
- Python Flask backend handling chatbot responses
- Docker configuration for easy deployment
- Mailhog for simulating bot forwarding emails to admin

## Technologies

- Vue.js
- Python Flask
- Docker
- Mailhog

## Getting Started

### Prerequisites

- Node.js
- npm
- Python
- Flask
- Docker
- Mailhog

### Installation

1. Clone the repository and change working directory into it:

```bash
git clone https://github.com/jeffmakuto/FAQ_Bot.git
cd FAQ_Bot
```

2. Install frontend dependencies:

```bash
cd front_end/bot_vue
```
Follow the setup instructions stipulated in the front_end directory README.md file - [Setup Frontend](./front_end/bot_vue/README.md).

3. Install backend dependencies (create a virtual environment if preferred):

```bash
cd back_end
```
Follow setup instructions stipulated in the back_end directory README.md file - [Setup Backend](./back_end/README.md).

## Docker

1. Create a docker network

```bash
docker network create mynetwork
```
Replace mynetwork with your desired network name.

2. Run frontend and backend containers attached to the created network:

For the Frontend (assuming you are in the `front_end/bot_vue` directory):
```bash
docker build -t front .
docker run --network=mynetwork -p 8080:80 --name frontend-container front
```

For the Backend (assuming you are in the root directory):
```bash
docker build -t back ./back_end
docker run --network=mynetwork -p 5000:5000 --name backend-container back
```

3. Run a new MailHog container with port 587 exposed

```bash
docker run --name=mailhog --network=mynetwork -p 1025:1025 -p 587:587 -p 8025:8025 -v $(pwd)/mailhog.crt:/etc/ssl/mailhog.crt -v $(pwd)/mailhog.key:/etc/ssl/mailhog.key mailhog/mailhog
```
4. To stop and remove the frontend and backend containers:

 ```bash
docker stop frontend-container
docker rm frontend-container
```
```
docker stop backend-container
docker rm backend-container

```
Stop and remove the existing MailHog container
```
docker stop mailhog
docker rm mailhog
```

**N/B: **If you've used different container names, replace `backend-container` and `frontend-container` with your actual container names.

## Configuration
Adjust configurations in the respective frontend and backend directories if needed.

## Usage
Access the chat interface by opening the provided frontend URL in a web browser.

## API Endpoints
* POST /bot: Send user input to the chatbot and receive responses.

## License

This project is licensed under the [Jeff Makuto Proprietary License](LICENSE).

© 2024 Jeff Makuto. All rights reserved.

