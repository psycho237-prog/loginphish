## Flask Login Logger

This project is a simple Flask web application that simulates a login page and logs user input, including email and password, to a text file. It is intended for educational purposes only.

### Requirements

- Python 3.x
- Flask

You can install Flask using pip:

```bash
pip install Flask
```

### Project Structure

```
/flask_login_logger
│
├── app.py                # Main application file
├── templates
│   └── login.html        # HTML template for the login page
└── log.txt               # File to log form data
```

### Usage

1. **Clone the Repository**: If you haven't already, clone the repository to your local machine.

2. **Navigate to the Project Directory**:

   ```bash
   cd flask_login_logger
   ```

3. **Run the Application**:

   ```bash
   python app.py
   ```

   or, if you are using Python 3:

   ```bash
   python3 app.py
   ```

4. **Access the Application**: Open your web browser and go to `http://127.0.0.1:8000/` to view the login page.

### How It Works

- **Login Page**: The root route (`/`) serves a login page rendered from `login.html`.

- **Data Logging**: 
  - When the user submits the login form, the `/steal` route captures the form data and appends it to `log.txt`.
  - The `/login` route simulates a login attempt by logging the email and password to `logs.txt` and returns a failure message.

### Important Notes

- **Educational Use Only**: This application is designed for educational purposes to demonstrate how to handle form data in Flask. It should not be used for malicious purposes.

- **Security**: The application does not implement any security measures. Do not use it in a production environment.

### License

This project is open-source and available for modification and distribution. Please ensure to credit the original authors if you use or modify the code.

### Acknowledgments

This project utilizes the Flask framework for web development. Feel free to contribute or suggest improvements!
