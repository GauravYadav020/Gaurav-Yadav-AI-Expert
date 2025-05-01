# Rename the file to main.py 

# ------------------------------------------------------
# 1) IMPORTS & SETUP
# ------------------------------------------------------
# - Import colorama for colored text
# - Import specific color constants (e.g., Fore, Style)
# - Import textblob for sentiment analysis
# - Initialize colorama for cross-platform color support

# ------------------------------------------------------
# 2) INITIAL GREETING
# ------------------------------------------------------
# - Print a welcome message using a color (e.g., Fore.CYAN)
# - Include emojis (e.g., '👋', '🕵️') for a fun greeting

# ------------------------------------------------------
# 3) USER NAME INPUT
# ------------------------------------------------------
# - Prompt the user for their name
# - Strip extra whitespace
# - If empty, default to "Mystery Agent"

# ------------------------------------------------------
# 4) CONVERSATION HISTORY
# ------------------------------------------------------
# - Create a structure (e.g., list) to store each user input
#   along with its polarity and sentiment type
# - For example: (user_text, polarity, sentiment_type)

# ------------------------------------------------------
# 5) INSTRUCTIONS
# ------------------------------------------------------
# - Print instructions to the user describing the available
#   commands (e.g., 'reset', 'history', 'exit')

# ------------------------------------------------------
# 6) MAIN INTERACTION LOOP
# ------------------------------------------------------
# - Use a 'while True:' loop to repeatedly prompt the user
# - Read input and strip whitespace
# - If empty, notify the user and continue

#     6.1) 'exit' COMMAND
#         - If user_input.lower() == 'exit':
#           - Print a farewell message
#           - Break out of the loop to end the program

#     6.2) 'reset' COMMAND
#         - Clear the conversation history
#         - Print a message confirming reset

#     6.3) 'history' COMMAND
#         - If no history, print a message indicating so
#         - Otherwise, print each conversation entry
#           - Show text, polarity (formatted), and sentiment type
#           - Use color and emojis based on sentiment
#         - Continue the loop

#     6.4) SENTIMENT ANALYSIS
#         - If the input is not a command, analyze sentiment
#         - Use TextBlob(user_input).sentiment.polarity to get a float
#           between -1.0 and +1.0
#         - Define thresholds:
#             > 0.25 -> Positive
#             < -0.25 -> Negative
#             Otherwise -> Neutral
#         - Assign color and emoji accordingly (e.g., GREEN/😊, RED/😢, YELLOW/😐)
#         - Append the tuple (text, polarity, sentiment_type) to the history
#         - Print a result message showing sentiment type and polarity

# ------------------------------------------------------
# END
# ------------------------------------------------------
# - The program terminates when 'exit' is typed
# - No additional code is shown beyond these comments
