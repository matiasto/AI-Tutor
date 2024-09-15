# AI-Tutor
## Getting Started
1. Ensure that you have Python 3.11 or later installed.
2. Install poetry by running:
    ```bash
    pip install poetry
    ```
3. Clone the repository and navigate to the project directory.
    ```bash
    git clone https://github.com/matiasto/AI-Tutor.git
4. Install the dependencies by running:
    ```bash
    poetry install
    ```
5. Create .env into the root of the project with these parameters:
    ```python
    API_KEY=<personal OpenAI api_key>
    LLM=<the model you want to use, e.g. 'gpt-4'>
6. Run the application by running:
    ```bash
    poetry run invoke start
    ```