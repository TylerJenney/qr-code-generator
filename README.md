# QR Code Generator (Dockerized Flask App)

A simple Flask web application that generates QR codes from user input. The app is containerized using Docker and requires no setup beyond a single command.

## Features

- Accepts user input via web form
- Generates a QR code image using `qrcode` and `Pillow`
- Dockerized for easy deployment and reuse
- No database required

## How to Run

### Option 1: Build Locally
docker build -t qr-code-app .

docker run -p 5000:5000 qr-code-app

Then open your browser and go to:
http://localhost:5000

### Option 2: Pull from Docker Hub
docker run -p 5000:5000 tylerjenney/qr-code-app

## Project Structure

qr-code-generator/
├── app.py
├── Dockerfile
├── requirements.txt
├── templates/
│   └── index.html
└── static/
    └── generated/

## Stack

- Python
- Flask
- qrcode
- Pillow
- Docker
