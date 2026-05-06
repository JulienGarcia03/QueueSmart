# QueueSmart

QueueSmart is a smart queue management application designed to improve customer wait experiences and help administrators efficiently manage queue operations. The system allows users to join queues digitally, monitor queue progress, and receive estimated wait-time information while administrators manage services, customers, and reporting.

This project was developed as a semester-long team project integrating frontend development, backend APIs, database persistence, reporting functionality, and smart queue features.

---

# Features

## Customer Features
- User registration and login
- Join available service queues
- View queue position and status
- Receive estimated wait-time information
- Queue tracking and notifications

## Administrator Features
- Manage services and queues
- View queue activity and customer information
- Generate queue activity reports
- Export reports as CSV files
- Access control for administrative pages

---

# Smart Feature

QueueSmart includes a smart wait-time estimation feature.

The system uses queue activity and queue position data to estimate how long a customer may need to wait before being served. This improves the user experience by helping customers make more informed decisions before joining a queue.

---

# Reporting Module

The reporting module allows administrators to generate reports containing:
- User queue participation history
- Queue activity information
- Service details
- Queue statistics and estimated durations

Reports can be exported as CSV files and are only accessible to administrator users.

---

# Technologies Used

- Python
- Django
- SQLite
- HTML/CSS
- Bootstrap
- JavaScript

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/JulienGarcia03/QueueSmart.git
cd QueueSmart
