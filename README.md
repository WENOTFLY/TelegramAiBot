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
/telegram_bot/
├── config/
│ ├── config.json # General settings (API, modes, permissions)
│ ├── models.json # AI model configurations (names, parameters)
│ ├── messages.json # Text messages (multilingual support)
│ ├── permissions.json # User roles and access control
│ ├── memory.json # Long-term user memory
│ ├── groups.json # Groups for posting
│ ├── moderation.json # Forbidden words list
│ ├── platforms.json # Platforms for posting (Telegram, VK, Discord)
│ └── .env # Environment variables (not included in Git)
│
├── modules/
│ ├── ai_integration.py # OpenWebUI API integration
│ ├── user_interaction.py # User interaction management
│ ├── post_generation.py # Post generation module
│ ├── buttons.py # Button generation (inline, reply)
│ ├── logging_handler.py # Logging system
│ ├── monitoring.py # System monitoring
│ ├── memory.py # Memory management (FSM)
│ ├── security.py # Security management (env variables)
│ └── access_control.py # Role and permission management
│
├── handlers/
│ ├── start_handler.py # /start command handler
│ ├── chat_handler.py # User message handler
│ ├── admin_handler.py # Owner/admin command handler
│ ├── post_handler.py # Post generation and publishing
│ ├── stats_handler.py # Usage statistics
│ ├── error_handler.py # Error handler
│ └── access_control.py # Access control verification
│
├── utils/
│ ├── file_manager.py # JSON file management
│ └── fsm_manager.py # Finite State Machine for user memory
│
├── main.py # Main bot script
├── Dockerfile # Docker configuration
├── requirements.txt # Python dependencies
└── README.md # Project documentation