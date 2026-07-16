### Steps to install

#### 1. Install python 3 and pip

```
.....
```


#### 2. Clone the repo

```bash
git clone https://github.com/Precious-Udoibok/Guest_Management_system.git
```

#### 3. Create a virtual environment and activate it.

```bash
python3 -m venv venv
source venv/bin/activate
```

#### 4. Run the following command to create an `.env` file from the existing `.env example` template.

```bash
cp .env-example .env or copy .env-example .env

```

#### 5. Install poetry

```bash
pip install poetry
```

#### 6. Use poetry to install all other dependencies

```bash
poetry install
```

#### 7. Install the pre-commit hook locally

```bash
poetry run pre-commit install
```

#### 8. Add your endpoints


#### 9. Run the server using uvicorn
Use the `--reload` option in development mode.

```bash
uvicorn app.main:app --reload
```
```