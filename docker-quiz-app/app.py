from flask import Flask, request, render_template_string

app = Flask(__name__)

QUESTIONS = [
    {"id": 1, "question": "What does 'docker run' do?", "options": ["Build image", "Start container", "Stop daemon", "Delete container"], "answer": 1},
    {"id": 2, "question": "Which file defines a Docker image?", "options": ["Dockerfile", "Dockerimage.txt", "docker-compose.yml", "Makefile"], "answer": 0},
    {"id": 3, "question": "Purpose of Docker Compose?", "options": ["Build images", "Manage multi-container apps", "Run single container", "Push to Hub"], "answer": 1},
    {"id": 4, "question": "Command to list running containers?", "options": ["docker ps", "docker images", "docker run", "docker stop"], "answer": 0},
    {"id": 5, "question": "What is a Docker volume for?", "options": ["Network config", "Persist data", "Expose ports", "Set env vars"], "answer": 1},
    {"id": 6, "question": "What is a Docker image layer?", "options": ["A network interface", "A read-only template", "A storage volume", "An environment variable"], "answer": 1},
    {"id": 7, "question": "How to stop a running Docker container?", "options": ["docker kill", "docker stop", "docker pause", "docker rm"], "answer": 1},
    {"id": 8, "question": "Command to remove a Docker image?", "options": ["docker stop", "docker rm", "docker rmi", "docker delete"], "answer": 2},
    {"id": 9, "question": "What is Docker Hub?", "options": ["Local image storage", "Cloud-based registry", "Container runtime", "Orchestration tool"], "answer": 1},
    {"id": 10, "question": "What is a Dockerfile instruction to copy files?", "options": ["RUN", "CMD", "COPY", "ADD"], "answer": 2},
    {"id": 11, "question": "What is the default network in Docker?", "options": ["bridge", "host", "none", "overlay"], "answer": 0},
    {"id": 12, "question": "How to expose a port in Dockerfile?", "options": ["PORT", "EXPOSE", "OPEN", "MAP"], "answer": 1},
    {"id": 13, "question": "What is the entry point of a Docker container?", "options": ["CMD", "RUN", "ENTRYPOINT", "USER"], "answer": 2},
    {"id": 14, "question": "How to set environment variables in Dockerfile?", "options": ["VAR", "ENV", "SET", "EXPORT"], "answer": 1},
    {"id": 15, "question": "What is Docker Swarm?", "options": ["Single-host container management", "Container orchestration tool", "Image building tool", "Network plugin"], "answer": 1},
    {"id": 16, "question": "What is Kubernetes?", "options": ["Docker alternative", "Container orchestration platform", "Image registry", "Monitoring tool"], "answer": 1},
    {"id": 17, "question": "What is a Docker service in Swarm?", "options": ["A single container", "A group of tasks", "A network configuration", "A storage volume"], "answer": 1},
    {"id": 18, "question": "How to scale a Docker service in Swarm?", "options": ["docker scale", "docker resize", "docker up --scale", "docker service scale"], "answer": 3},
    {"id": 19, "question": "What is a pod in Kubernetes?", "options": ["A single container", "Smallest deployable unit", "A network policy", "A storage class"], "answer": 1},
    {"id": 20, "question": "What is a Kubernetes deployment?", "options": ["Networking rule", "Manages replica sets", "Storage configuration", "Security setting"], "answer": 1},
    {"id": 21, "question": "What is a Kubernetes service?", "options": ["Exposes applications", "Defines storage", "Configures networking", "Manages security"], "answer": 0},
    {"id": 22, "question": "What is Helm in Kubernetes?", "options": ["Security tool", "Package manager", "Monitoring agent", "Networking plugin"], "answer": 1},
    {"id": 23, "question": "What is a Dockerfile instruction to execute commands?", "options": ["COPY", "ADD", "ENV", "RUN"], "answer": 3},
    {"id": 24, "question": "What is the purpose of '.dockerignore' file?", "options": ["Ignore image layers", "Exclude files from image", "Define network rules", "Set environment variables"], "answer": 1},
    {"id": 25, "question": "What is a container registry?", "options": ["Local storage only", "Centralized image storage", "Network configuration file", "Container runtime engine"], "answer": 1},
]

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Docker Quiz</title>
    <style>
        body {
            font-family: sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .quiz-container {
            background-color: #fff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 80%;
            max-width: 600px;
        }
        h1 {
            color: #333;
            text-align: center;
            margin-bottom: 20px;
        }
        .question-container {
            margin-bottom: 20px;
            padding: 15px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        .question-container:not(:first-child) {
            display: none; /* Initially hide all questions except the first */
        }
        p strong {
            color: #007bff;
            font-size: 1.1em;
            display: block;
            margin-bottom: 10px;
        }
        label {
            display: block;
            margin-bottom: 8px;
            color: #555;
        }
        input[type="radio"] {
            margin-right: 8px;
        }
        .controls {
            text-align: center;
            margin-top: 20px;
        }
        button {
            background-color: #007bff;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 1em;
            margin: 0 10px;
            transition: background-color 0.3s ease;
        }
        button:hover {
            background-color: #0056b3;
        }
        #submit-button {
            background-color: #28a745;
        }
        #submit-button:hover {
            background-color: #218838;
        }
        .hidden {
            display: none !important;
        }
        .congrats {
            background-color: #d4edda;
            color: #155724;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: center;
            font-size: 1.5em;
            margin-top: 30px;
        }
    </style>
</head>
<body>
    <div class="quiz-container">
        <h1>Docker Quiz</h1>
        <form method="post" action="/submit" id="quiz-form">
            {% for q in questions %}
                <div class="question-container" id="question{{ q.id }}">
                    <p><strong>{{ loop.index }}. {{ q.question }}</strong></p>
                    {% for opt in q.options %}
                        <label>
                            <input type="radio" name="q{{ q.id }}" value="{{ loop.index0 }}" required>
                            {{ opt }}
                        </label><br>
                    {% endfor %}
                </div>
            {% endfor %}
            <div class="controls">
                <button type="button" id="prev-button" disabled>Previous</button>
                <button type="button" id="next-button">Next</button>
                <button type="submit" id="submit-button" class="hidden">Submit Quiz</button>
            </div>
        </form>
    </div>

    <script>
        const questionContainers = document.querySelectorAll('.question-container');
        const prevButton = document.getElementById('prev-button');
        const nextButton = document.getElementById('next-button');
        const submitButton = document.getElementById('submit-button');
        const totalQuestions = questionContainers.length;
        let currentQuestionIndex = 0;

        function showQuestion(index) {
            questionContainers.forEach((container, i) => {
                container.style.display = i === index ? 'block' : 'none';
            });

            prevButton.disabled = index === 0;
            nextButton.textContent = index === totalQuestions - 1 ? 'Submit Quiz' : 'Next';
            submitButton.classList.toggle('hidden', index !== totalQuestions - 1);
            nextButton.removeEventListener('click', nextQuestion); // Remove previous listener
            if (index === totalQuestions - 1) {
                nextButton.addEventListener('click', submitQuiz);
            } else {
                nextButton.addEventListener('click', nextQuestion);
            }
        }

        function nextQuestion() {
            if (currentQuestionIndex < totalQuestions - 1) {
                currentQuestionIndex++;
                showQuestion(currentQuestionIndex);
            }
        }

        function prevQuestion() {
            if (currentQuestionIndex > 0) {
                currentQuestionIndex--;
                showQuestion(currentQuestionIndex);
            }
        }

        function submitQuiz() {
            document.getElementById('quiz-form').submit();
        }

        prevButton.addEventListener('click', prevQuestion);
        showQuestion(currentQuestionIndex); // Show the first question initially
    </script>
</body>
</html>
'''

@app.route('/', methods=['GET'])
def index():
    return render_template_string(HTML_TEMPLATE, questions=QUESTIONS)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    total = len(QUESTIONS)
    for q in QUESTIONS:
        question_id = str(q['id'])
        ans = request.form.get(f"q{question_id}")
        if ans is not None:
            try:
                submitted_answer = int(ans)
                if submitted_answer == q['answer']:
                    score += 1
            except ValueError:
                print(f"Warning: Invalid answer submitted for question {question_id}: {ans}")
        else:
            print(f"Warning: No answer submitted for question {question_id}")

    congrats_message = ""
    if score == total:
        congrats_message = "<div class='congrats'>🥳 👏 Congratulations! 🎉 You got a perfect score: {} / {}! 🌟 Cheers! 🥂</div>".format(score, total)
    else:
        congrats_message = "<div class='congrats'>Your Score: {} / {}</div>".format(score, total)

    return f"""
    <style>
        body {{
            font-family: sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }}
        .congrats {{
            background-color: #d4edda;
            color: #155724;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: center;
            font-size: 1.5em;
            margin-top: 30px;
        }}
    </style>
    {congrats_message}
    """

if __name__ == '__main__':
    app.run(debug=True)
