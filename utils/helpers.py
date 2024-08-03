# utils/helpers.py

def format_message(message):
    """
    Format a message with basic sanitization or styling.
    """
    return message.strip().capitalize()

def log_error(error_message):
    """
    Log errors to the console or a log file.
    """
    print(f"ERROR: {error_message}")

def get_user_info(user_id, db):
    """
    Fetch user information from the database.
    """
    # Example: Replace with actual database fetch code
    user_info = db.get_user(user_id)
    return user_info

def fetch_status():
    """
    Fetch the status of the bot or server.
    """
    # Example: This could be a call to an external service or a status check
    return "All systems operational"
