# Grammar-Based Blackbox Fuzzer for SQLite

This project implements a grammar-based fuzzer to test the SQLite database engine.

## 🔧 How It Works

- `grammar.py`: Defines a flexible SQL grammar based on the SQLite command reference.
- `fuzzer.py`: Uses the grammar to generate diverse SQL inputs.
- `run.py`: Executes inputs on SQLite, collects coverage metrics, and produces output reports.

## 🚀 How to Run

1. Clone the repository:
   git clone https://github.com/YOUR_USERNAME/sqlite-fuzzer.git
   cd sqlite-fuzzer

2. Build and run the Docker container (optional if you want the same environment):
   docker build -t sqlite-fuzzer
   docker run -it sqlite-fuzzer
   
3. Generate inputs and coverage:
   python3.10 run.py 1000
   python3.10 run.py --plot-every-x 100 1000
   
4. Get detailed coverage:
   make coverage-html

## 📊 Output
coverage_report.csv — basic summary of branch coverage.
plot.pdf — visual plot of coverage over time.
coverage_report.html — detailed interactive report (after running make coverage-html).

## 🛠️ Environment

Python 3.10
Docker
SQLite

## 📄 Note
Only fuzzer.py and grammar.py were modified in this project. All other files are part of the base framework.
