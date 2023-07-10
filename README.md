# DevRev-Flight-Ticket-Booking

This is a web application for flight ticket booking, allowing users to search for flights, make bookings, and admin to
manage flights.

## Features

- User Registration and Authentication: Users can sign up and log in to the application to access their account and make
  bookings.
- Flight Search: Users can search for flights based on their origin, destination, departure date, and time.
- Flight Booking: Users can book tickets for available flights and select their preferred seats.
- My Bookings: Users can view their booking history, including details of their upcoming and past flights.
- Admin Dashboard: Admin users have access to an administration dashboard for managing flights and viewing bookings

## Technologies Used

- Python
- Django Framework
- HTML
- CSS

## Setup and Installation

1. Clone the repository:

```commandline
    git clone https://github.com/muthuruban/DevRev-Flight-Ticket-Booking/tree/main
```

2. Install the required dependencies:

```commandline
    pip install -r requirements.txt
```

3. Change to the directory:

```commandline
    cd DevRev-Flight-Ticket-Booking/
```

4. Run the database migrations:

```commandline
  python manage.py migrate 
```

5. Start the development server:

```commandline
   python manage.py runserver
```

6. Access the application in your web browser at `http://localhost:8000`.

7. Admin Login Details:

```
  adminname: admin
  password: admin123
```

8. User Login Details:

```
  username: sampleuser
  password: user@123
```
9. Available Flight Lists:

- Flight Number: DLE44567 Airline: Air India From: Delhi To: Mumbai Departure Date & Time: July 13, 2023  14:45:00
- Flight Number: 3458398 Airline: Jet Airways From: Madurai To: Chennai Departure Date & Time: July 14, 2023  12:45:00	
- Flight Number: 3458398 Airline: IndiGo From: Delhi To: London Departure Date & Time: July 15, 2023  18:50:00
- Flight Number: EF890651 Airline: British Airways From: Delhi To: Sandtoft Departure Date & Time: July 18, 2023  03:00:00
- Flight Number: LB593089E Airline: American Airlines From: Denver To: Mumbai Departure Date & Time: July 20, 2023  23:00:00

## Project Structure

The project follows the following structure:

- `mainapp/`: Contains the main application files, auxiliary app for managing booking-related models.
- `migrations/`: Database migration files.
- `static/`: Static files such as CSS, images, and JavaScript.
- `templates/`: HTML templates for rendering the web pages.
- `admin.py`: Django admin configuration.
- `models.py`: Application models.
- `forms.py`: Custom forms for user input validation.
- `urls.py`: URL routing configuration.
- `views.py`: View functions to handle HTTP requests.
- `flight_booking/`: Contains the `settings.py` and `urls.py` for the mainapp.
- `manage.py`: Django command-line utility for managing the project.

## Database Structure

![alt text](https://github.com/muthuruban/DevRev-Flight-Ticket-Booking/blob/main/dbimg.png?raw=true)

## Contributing

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please feel
free to submit a pull request or create an issue.

## Link

[Flight Ticket Booking - https://muthuruban.pythonanywhere.com/](https://muthuruban.pythonanywhere.com/)
