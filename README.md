# Quizzy App
A web-based platform for creating,traking and managing quzzes.
## Features
- User authentication and profile management
- Timer and progress tracking
- Multiple quiz categories and difficulty levels
- Detailed performance analytics with feedback
## Installation
1. Clone the repository:
```
    git clone https://{YOUR_PERSONAL_TOKEN}@github.com/{YOUR_USERNAME}/quz-app.git
```
2. Navigate to the project:
```
    cd quiz-app.git
```
3. Set up virtual environment (optional but recommended):
```
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Script\activate
```
4. Install dependencies:
```
    pip install -r requirements.txt
```
5. Apply database migrations:
```
    python manage.py migrate
```
6. Run the development server:
```
    python manage.py runserver
```
7. Open browser and navigate to: http://127.0.0.1:8000
## Usage
1. Register or log in your account.
2. Browse or search for quizzes by category or difficulty.
3. Start a quiz, answer questions, and submit your results.
4. View your performance and detailed feedback for each quiz.
## Contributing
Contributions are welcome! Follow these steps to contribute:
1. Fork the repository.
2. Create a feature branch:
```
    git checkout -b feature-name
```
3. Commit your changes:
```
    git commit -m "Add feature-name"
```
4. Push to branch:
```
    git push origin feature-name
```
5. Open a pull request.
## License
This project is licensed under the MIT License. See the LICENSE file for more details.
## Contact
For questions or support, contact francmaki14@gmail.com.
