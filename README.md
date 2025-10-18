# Diary-Tur

Diary-Tur is a personal diary web application that allows users to securely store and manage their daily thoughts and experiences.

## Table of Contents

* [Features](#features)
* [Technologies](#technologies)
* [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)

## Features

* Add, view, and manage daily diary entries.
* Secure local storage using SQLite.
* Clean and responsive web interface.

## Technologies

* **Python**: Backend server logic.
* **Flask**: Web framework.
* **HTML / CSS**: Frontend design.
* **SQLite**: Local database for storing diary entries.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/enis1enis2/diary-tur.git
   cd diary-tur
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python main.py
   ```

5. Open your browser and go to `http://127.0.0.1:5000`.

## Usage

* Navigate to the web interface.
* Add new diary entries using the provided form.
* View existing entries on the main page.

## Contributing

Contributions are welcome! Follow these steps:

1. Fork the repository.
2. Create a new branch:

   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit:

   ```bash
   git commit -m "Add some feature"
   ```
4. Push to your branch:

   ```bash
   git push origin feature-name
   ```
5. Open a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
