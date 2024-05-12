# Ko Bancha Karod Pati

## Introduction

"Ko Bancha Karod Pati" is a Nepali version of the popular game "Who Wants to Be a Millionaire?". This game allows players to answer multiple-choice questions to win money based on their knowledge. It is developed using Tkinter library in Python for the graphical user interface.

## Features

- Multiple-choice questions covering various topics related to Nepal.
- Customizable username and password for login.
- Dynamic question generation to ensure a unique experience in each session.
- Real-time feedback on answers with correct/incorrect indications.
- Accumulated money display throughout the game.
- End-of-game message displaying the total money earned.

## How to Play

1. **Login**: Enter your username and password to access the game.  [Default Pass word is '1234'], and [Default User are admin, Admin, user]
   ## Note : You can add username by changing the username List 'UsernameList', and default password with 'Default_password';
3. **Answer Questions**: Answer multiple-choice questions displayed on the screen.
4. **Win Money**: Earn money for each correct answer. The amount increases with each correct response.
5. **End of Game**: When all questions are answered, the game concludes, and your total earnings are displayed.

## Installation

1. Ensure you have Python installed on your system.
2. Clone or download the repository containing the game code.
3. Navigate to the directory containing the code.
4. Run the game using the following command:
python Ko_Bancha_Karod_Pati.py

## Customization

- **Questions and Answers**: Add or modify questions and answer options in the `Question` list within the code.

### Format:
```bash
Question = [
    {
        "Que": "Question here ?",
        "options": ["A) option 1", "B) option", "C) option", "D) option"],
        "answer": "0"
    },
```



- **Username and Password**: Adjust the list of usernames and password in the `UsernameList` variable to control access to the game.
- **User Interface**: Customize the appearance of the game window and widgets using Tkinter attributes.

## Code Structure

- **Main Window Class (`window`)**: Represents the main application window and manages navigation between login and game pages.
- **Login Page Class (`login_page`)**: Handles user authentication and provides access to the game page upon successful login.
- **Game Page Class (`Game_page`)**: Displays questions, options, and tracks player progress and earnings during the game.
- **Question Data (`Question`)**: Contains a list of dictionaries, each representing a question, its options, and the correct answer.

## Dependencies

- `customtkinter`: A custom library for enhancing Tkinter widgets and styling. Ensure it is included in the project directory or install it via the `requirements.txt` file.


