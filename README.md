
# 🚀 Telegram Bot with Advanced Role System, Post Generation, and Multilingual Support

## 📌 Project Overview
This project is an advanced, modular, and secure Telegram bot designed for content creation, post publishing, and user management. It supports:

- ✅ Flexible role management (Owner, Admin, Moderator, Editor, User).
- ✅ Post generation using OpenWebUI API with customizable templates.
- ✅ Multi-platform posting (Telegram, VK, Discord).
- ✅ Multilingual support (Russian, English, and more).
- ✅ Advanced monitoring, logging, and analytics.
- ✅ Secure environment configuration with `.env`.


## 🌐 Key Features
- **Role-Based Access Control:** Fully configurable user roles with customizable permissions.
- **Secure Configuration:** API keys and sensitive data stored securely in `.env`.
- **Multi-Platform Posting:** Supports posting to multiple platforms (Telegram, VK, Discord).
- **Advanced Post Generation:** Generate and edit posts with AI (OpenWebUI API).
- **Multi-Language Support:** User interface available in multiple languages.
- **Monitoring and Analytics:** Detailed usage statistics, error logging, and user activity tracking.
- **Memory Management:** Contextual memory for user interactions and generated posts.

## 📁 Project Structure
```
/telegram_bot/
├── config/
│   ├── config.json          # General settings (API, modes, permissions)
│   ├── models.json          # AI model configurations (names, parameters)
│   ├── messages.json        # Text messages (multilingual support)
│   ├── permissions.json     # User roles and access control
│   ├── memory.json          # Long-term user memory
│   ├── groups.json          # Groups for posting
│   ├── moderation.json      # Forbidden words list
│   ├── platforms.json       # Platforms for posting (Telegram, VK, Discord)
│   └── .env                 # Environment variables (not included in Git)
│
├── modules/
│   ├── ai_integration.py    # OpenWebUI API integration
│   ├── user_interaction.py  # User interaction management
│   ├── post_generation.py   # Post generation module
│   ├── buttons.py           # Button generation (inline, reply)
│   ├── logging_handler.py   # Logging system
│   ├── monitoring.py        # System monitoring
│   ├── memory.py            # Memory management (FSM)
│   ├── security.py          # Security management (env variables)
│   └── access_control.py    # Role and permission management
│
├── handlers/
│   ├── start_handler.py     # /start command handler
│   ├── chat_handler.py      # User message handler
│   ├── admin_handler.py     # Owner/admin command handler
│   ├── post_handler.py      # Post generation and publishing
│   ├── stats_handler.py     # Usage statistics
│   ├── error_handler.py     # Error handler
│   └── access_control.py    # Access control verification
│
├── utils/
│   ├── file_manager.py      # JSON file management
│   └── fsm_manager.py       # Finite State Machine for user memory
│
├── main.py                  # Main bot script
├── Dockerfile               # Docker configuration
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## 🚀 Getting Started
### Prerequisites
- Python 3.8+
- A Telegram bot token (from BotFather)
- OpenWebUI API running and accessible

### Installation
1. Clone this repository:
```bash
git clone https://github.com/WENOTFLY/telegram_bot.git
cd telegram_bot
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file:
```bash
TELEGRAM_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
OPENWEBUI_API_URL=http://localhost:3000
LOGGING_LEVEL=INFO
```

4. Configure user roles in `config/permissions.json`.

### Running the Bot
```bash
python main.py
```

### Docker Setup
1. Build Docker image:
```bash
docker build -t telegram_bot .
```

2. Run Docker container:
```bash
docker run -d --name telegram_bot -p 8000:8000 telegram_bot
```

## 📌 Usage
- Use `/start` to begin interacting with the bot.
- Use `/generate_post` to generate and publish a post.
- Use `/stats` to view bot usage statistics.
- Use `/roles` to list available roles and permissions.

## 🚀 Role Management
- Use `/roles` to view all available roles and their permissions.
- Use `/add_role` to assign a role to a user (owner only).
- Use `/remove_role` to revoke a role from a user (owner only).
- Use `/list_roles` to list all users with their roles.

## 📊 Monitoring and Analytics
- View user activity statistics with `/stats` (owner/admin only).
- Access detailed logs for error tracking.

## 📄 License
This project is licensed under the MIT License.


## 📌 Управление логами
- 📊 Просмотр логов (для владельца): `/logs`
- Логи хранятся в папке `logs/` с ежедневной ротацией файлов.
- Просмотр последних 20 строк логов.

