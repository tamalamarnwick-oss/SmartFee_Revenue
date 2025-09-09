# CWED_SmartFee_Revenue_Collection System

A comprehensive Revenue Collection software designed for educational institutions to manage PTA Fund, School Development Fund (SDF), Boarding Fee and Other Income payments for the School.

## Features

### Core Functionality
- **Student Management**: Add and manage student records with fee requirements
- **Income Tracking**: Record payments for PTA Fund and SDF separately
- **Expenditure Management**: Track expenses for both fund types
- **Payment Status**: Monitor which students have paid in full vs outstanding balances
- **Receipt Generation**: Printable receipts for students who have completed all payments
- **SMS Reminders**: Send payment reminders to parents (integration ready)

### Reporting
- **Daily Reports**: Detailed financial reports for any specific date
- **Weekly Reports**: Comprehensive 7-day financial summaries
- **Fund Separation**: Separate tracking and reporting for PTA and SDF funds
- **Real-time Dashboard**: Live statistics and quick actions

## Installation

1. **Install Python Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**:
   ```bash
   python app.py
   ```

3. **Access the System**:
   Open your web browser and go to `http://localhost:5000`

## Usage Guide

### Getting Started
1. **Add Students**: Start by adding student records with their fee requirements
2. **Record Payments**: Log payments as they come in, specifying PTA or SDF
3. **Track Expenditures**: Record any expenses from either fund
4. **Generate Reports**: Create daily/weekly financial reports
5. **Monitor Status**: Check payment status and generate receipts

## Technical Details

### Technology Stack
- **Backend**: Flask (Python web framework)
- **Database**: SQLite (lightweight, file-based)
- **Frontend**: Bootstrap 5 + HTML/CSS/JavaScript
- **Icons**: Font Awesome

### Database Schema
- **Students**: ID, name, class, phone, balances, requirements
- **Income**: Payment records with student info and amounts
- **Expenditure**: Expense records with activity details

## SMS Integration

The system includes SMS reminder functionality that can be integrated with services like Twilio, AWS SNS, or other SMS gateway providers.

## Security Notes

- Change the SECRET_KEY in `app.py` for production use
- Use environment variables for sensitive configuration
- Consider using a more robust database for production

## Support

For questions or support, refer to the code documentation or contact the system administrator.
