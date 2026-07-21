class ApplicationLogger:
    _sole_instance = None

    def __new__(cls):
        # Create singleton instance if none exists
        if cls._sole_instance is None:
            cls._sole_instance = super(ApplicationLogger, cls).__new__(cls)
            print("Logger instance created.")
        return cls._sole_instance

    def log_message(self, text):
        print(f"[SYSTEM LOG]: {text}")


# Initialize two logger references
primary_logger = ApplicationLogger()
secondary_logger = ApplicationLogger()

# Ensure both reference the exact same object
print(f"Is primary_logger the same instance as secondary_logger? {primary_logger is secondary_logger}")

# Execute test logs
primary_logger.log_message("Initial message from primary logger.")
secondary_logger.log_message("Subsequent message from secondary logger.")