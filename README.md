# ETL Pipeline Project

## Overview

This project is a simple ETL (Extract, Transform, Load) pipeline built using Python, Pandas, Parquet, and MySQL.

The pipeline extracts data from DummyJSON APIs, transforms and cleans the data, and loads it into a MySQL database.

---

## Tech Stack

* Python
* Pandas
* PyArrow
* MySQL
* Git
* GitHub

---

## Project Structure

```text
ETL/
├── extract.py
├── transform.py
├── load.py
├── config.py
├── .gitignore
├── README.md
```

---

## ETL Flow

### Extract

* Fetches data from DummyJSON APIs
* Supports pagination
* Handles HTTP errors
* Saves raw data as Parquet files

### Transform

* Uses pandas for cleaning and normalization
* Handles nested JSON structures
* Splits data into entities:

  * Products
  * Reviews
  * Users
  * Address
  * Credentials
  * Carts

### Load

* Loads transformed data into MySQL tables
* Uses reusable loading functions
* Uses batch inserts with executemany()

---

## Features

* API pagination
* Error handling
* Reusable ETL functions
* Parquet-based storage
* MySQL integration

---

## Learning Outcomes

This project helped me learn:

* ETL pipeline development
* API data extraction
* Data transformation using Pandas
* Loading data into relational databases
* Git and GitHub workflows
* Version control using branches and merges
