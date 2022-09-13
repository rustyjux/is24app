# FizzBuzz Testing

## Requirements
- Python 3
- Libraries: `pytest`, `pytest-cov`, `junit2html`

## Use
- Create a virtual environment (Python 3: `python -m venv virtenv`) and activate
- Install dependencies (`pip install -r requirements.txt`)
- Run test (`pytest` or `pytest --cov=fizzbuzz --cov-report=term-missing` for coverage report)
- To export report:
    - run test w/ junitxml output (`pytest --cov=fizzbuzz --junitxml=result.xml`)
    - convert junit to html report (`junit2html results.xml results.html`)