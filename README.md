# TestHi Telegram Bot

![Telegram Bot](https://github.com/miyaxyzz/testhi/blob/main/assets/telegram_bot.png)

*A simple Telegram bot for testing and greeting users.*

## Features

- Sends a welcome message to new users who join the chat.
- Responds to user commands and provides appropriate replies.
- Implements basic functionality for testing purposes.
- Easy to set up and use.

## Usage

1. Start a chat with the [TestHi Bot](https://t.me/testhi_bot) on Telegram.
2. Send the `/start` command to begin using the bot.
3. Explore the available commands and interact with the bot.

## Deployment

To deploy the TestHi Telegram bot on your own server:

1. Clone this repository:
   ```
   git clone https://github.com/miyaxyzz/testhi.git
   ```
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Create a new bot using the [BotFather](https://core.telegram.org/bots#botfather) on Telegram and obtain the bot token.

4. Update the `config.py` file with your bot token:
   ```python
   # Telegram bot token
   BOT_TOKEN = 'YOUR_BOT_TOKEN'
   ```

5. Run the bot:
   ```
   python3 bot.py
   ```

The bot will start running, and you can interact with it on Telegram.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open a GitHub issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).