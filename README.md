[![Automated Testing](https://github.com/komax-go-cart/backend/actions/workflows/python.yml/badge.svg)](https://github.com/komax-go-cart/backend/actions/workflows/python.yml)

# Backend
Backend API to provide sensor data using WebSockets.

# 🛠 Setting up the Development environment

This project uses python virtual environments [venv](https://docs.python.org/3/library/venv.html) to enable lightweight independent package installations. So to start setting up this project. You will need to run one of the following commands:

### Windows

```bash
.\.venv\Scripts\activate.bat
```

```bash
.\.venv\bin\Activate.ps1
```

### Linux or Mac

```bash
source .venv/bin/activate
```

Next, you must install the necessary dependencies and python packages via pip. For easier installation, we created requirements.txt you can install it like this:



```bash
pip install -r requirements.txt
```

# ♻️ Testing

To execute all unit tests we implemented the [pytest](https://docs.pytest.org/en/7.2.x/) library. An automatic GitHub action is also in place. It executes on every push to the main branch or after the creation of a pull request. To run it locally on your device execute the command in the repositories root directory:

```bash
pytest
```

# Docker Container Start
Buil Dockerfile in the root directory.

```
docker build -t gokart:1 .
```

Docker Container starten
```
docker run -t 80:80 gokart:1
```