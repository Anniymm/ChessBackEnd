
## ❗Branches
Review the different branches for specific parts of the project. Once reviewed, merge requests can be created as needed.(For main functionality and final version, see dashboard branch)
# Project Management Web Application
A comprehensive web application designed for efficient project management, tailored to facilitate smooth collaboration between clients and contractors. The application uses a chess clock principle to track task progress timelines and identify the responsible party during specific periods.


## Key Features

### 1. Project Timelines and Progress Monitoring
- **Real-time Updates:** Display project timelines and current status in real time.
- **Progress Monitoring:** Visual representation of which party (client or contractor) is responsible for task progress.
- **Individual Hour Calculation:** Track and calculate individual hours spent by both client and contractor, including details on responsibility transfers and periods of inactivity.

### 2. Responsibility Transfer Timer (Chess Clock)
- **Timer Functionality:**
  - Starts for the contractor when work can commence, showing a countdown to the project deadline.
  - Starts for the client when questions arise, halting work if the questions are critical and awaiting a mandatory response.
- **Types of Questions:**
  - **Mandatory Questions:** Critical questions that, if unanswered, pause the project.
  - **Non-Mandatory Questions:** Questions that do not affect the project timeline.
- **Responsibility Indicator:** Both parties can view which side the timer is on, who needs to respond, and how long the timer has been running.
- **End-of-Project Reporting:** Generates detailed reports on time tracking and responsibility switches.

### 3. Communication Features
- **Question and Answer Management:**
  - Upload and manage questions and answers within the application.
  - Automatic email notifications for all project members.
- **Link Generation:** A secure link is generated for clients to view questions and provide answers, with verification to prevent unauthorized access.
- **File Upload Functionality:** Ability to upload files related to questions or responses.
- **Mandatory Question Alerts:** Warnings issued if a mandatory question is unanswered, affecting the timer's status.
- **Owner Privileges:** The project owner can modify dates, edit or remove questions, and change priorities.
- **Client Request Rights:** Clients can request changes to project details, pending owner approval.

### 4. Reporting
- **Contract Term Display:** Original contract term and any updates.
- **Actual Term Calculation:** Updated term based on project progress and delays.
- **Time Summary:** Detailed breakdown of time spent by the client and contractor.
- **Fair Deadline Calculation:** Adjusted deadline considering delays caused by both parties.


## Additional Features
- **Dashboard:** Overview of all projects created by the user.
- **Project Summary:** Essential details, including deadlines, status, and the responsible party.

## Getting Started

### Prerequisites
- Install [Python](https://www.python.org/) and [Django](https://www.djangoproject.com/) for the backend.
- Set up a database (e.g., PostgreSQL or MySQL) for data management.

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Anniymm/ChessBackEnd.git
   ```
## Installation Instructions

1. **Navigate to the project directory:**
   ```bash
   cd ChessBackEnd
   ```
2. install:
   ```bash
   pip  install -r requirements.txt
   ```
3. Run:
   ```bash
   python manage.py runserver
   ```
   
