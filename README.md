# 🚀 Milestone 1: Environment Setup & Pipeline Design

## 📌 Overview

This milestone focuses on building the **foundation of the High Throughput Log Processing System**.
It includes environment configuration, distributed processing setup, and designing a scalable log ingestion pipeline.

---

## 🎯 Objective

* Set up Python development environment
* Configure distributed frameworks (**Dask & Ray**)
* Design log ingestion pipeline
* Define structured schemas for logs and anomalies

---

## 🛠️ Tech Stack

* **Python 3.x**
* **Dask** – Parallel computing
* **Ray** – Distributed execution
* **YAML** – Schema definitions

---

## ⚙️ Environment Setup

### Step 1: Clone Repository

```bash
git clone <your-repo-link>
cd project-folder
```

### Step 2: Create Virtual Environment

```bash
python -m venv .venv
```

### Step 3: Activate Environment

```bash
# Windows
.venv\Scripts\activate

# Linux / Mac
source .venv/bin/activate
```

### Step 4: Install Dependencies

```bash
pip install -r environment/requirements.txt
```

---

## 🧩 Project Structure

```
project/
│
├── environment/
│   └── requirements.txt
│
├── schemas/
│   ├── log_schema.yaml
│   └── anomaly_schema.yaml
│
├── ingestion.py
├── parser.py
├── log_generator.py
├── dask_pipeline.py
├── ray_pipeline.py
├── main.py
│
└── tests/
    └── test_environment.py
```

---

## 🔄 Pipeline Design

The log processing pipeline consists of the following stages:

1. **Log Generation**

   * Generates sample logs using `log_generator.py`

2. **Ingestion**

   * Reads and streams logs into the system (`ingestion.py`)

3. **Parsing**

   * Converts raw logs into structured format (`parser.py`)

4. **Distributed Processing**

   * Uses:

     * `dask_pipeline.py` for parallel execution
     * `ray_pipeline.py` for distributed tasks

---

## 📊 Schema Design

### 🔹 Log Schema

Defines structure of incoming logs:

* timestamp
* log level
* message
* source

### 🔹 Anomaly Schema

Defines structure for anomaly detection:

* anomaly type
* severity
* detected timestamp
* metadata

---

## ▶️ Running the Project

```bash
python main.py
```

---

## 🧪 Testing Environment

```bash
pytest tests/test_environment.py
```

---

## ✅ Outcome of Milestone 1

* Successfully configured development environment
* Implemented distributed processing using Dask & Ray
* Designed scalable log ingestion pipeline
* Defined structured schemas for logs and anomalies

---

## 🚀 Next Steps

* Implement anomaly detection logic
* Add real-time processing capabilities
* Integrate visualization/dashboard


## 📜 License

This project follows the MIT License.
