This bot is a convenient tool for job searching and posting job vacancies directly on Telegram.
When you start the bot, it immediately offers you two options:
Find a job: When you press this button, the bot asks you to enter a job title (e.g., "Programmer"). Then it searches for jobs based on this query:
In its local database, where job listings have already been added by other users.
It also makes a request to the hh.kz website to show the most up-to-date vacancies from the internet.
Post a job vacancy: If you want to add a vacancy, the bot asks you to enter the information in the following format:
nginx
Копировать
Редактировать
Job Title - City - Salary - Description
For example:
Python Developer - Almaty - 600000 - Remote work, experience from 2 years.
The bot saves this job listing in its database, and it becomes available for other users to search.
All job data is stored in an SQLite database, and you can always refer back to it. The bot helps you quickly find job information or post your own vacancy.
So, this bot does two useful things:
It helps you find a job, both in the bot's database and on hh.kz.
It gives you the ability to post your own job vacancy so other users can find it.
It’s really convenient when you need to quickly and easily find a job or share a vacancy!
In this code, the following libraries are used:
1. **`asyncio`**: This is a built-in Python library that helps with writing asynchronous programs. It allows the bot to handle multiple tasks at once, like processing messages and making API calls, without slowing down the bot.
2. **`logging`**: This standard Python library is used for tracking and recording events and errors in the bot's operations. It helps the developers keep an eye on what’s going on with the bot and catch any issues that may arise.
3. **`sqlite3`**: A built-in library in Python used to work with SQLite databases. This is what stores all the job listings and other data in the bot. It’s lightweight and perfect for small databases like the one used here.
4. **`requests`**: This is a popular Python library that makes it easy to send HTTP requests. In this bot, it’s used to interact with the **hh.kz API**, which helps pull real-time job listings from the website.
5. **`aiogram`**: This is the library used to build the Telegram bot itself. It makes it simple to interact with Telegram’s API, handle messages, and create inline buttons. Some of the important components from this library are:
   - **`Bot`**: The bot object, which represents the bot itself.
   - **`Dispatcher`**: The part that handles how the bot reacts to messages and events.
   - **`types`**: This module contains types for all kinds of objects the bot deals with, like messages and buttons.
   - **`InlineKeyboardMarkup` and `InlineKeyboardButton`**: These are used to create interactive buttons in the bot’s messages.
Together, these libraries help the bot function smoothly, allowing it to fetch job listings, store data, and interact with users in Telegram.
![image](https://github.com/user-attachments/assets/ac4e175c-69f0-473c-8ca5-b848e2191012)


