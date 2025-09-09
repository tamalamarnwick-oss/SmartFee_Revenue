# SmartFee Revenue Collection System - Render Deployment Guide

## Prerequisites
- Render account
- GitHub repository with the application code

## Environment Variables Required on Render

Set these environment variables in your Render service:

### Required Variables
```
SECRET_KEY=your-super-secret-key-change-this-in-production
DEFAULT_USERNAME=your-developer-username
DEFAULT_PASSWORD=your-developer-password
DEV_USERNAME=your-developer-username
DEV_PASSWORD=your-developer-password
DATABASE_URL=postgresql://... (Render will provide this automatically)
FLASK_ENV=production
```

### Optional SMS Variables
```
AFRICASTALKING_USERNAME=your-sms-username
AFRICASTALKING_API_KEY=your-sms-api-key
SMS_SENDER_ID=SmartFee
```

## Deployment Steps

1. **Create PostgreSQL Database**
   - In Render dashboard, create a new PostgreSQL database
   - Note the database URL (will be auto-set as DATABASE_URL)

2. **Create Web Service**
   - Connect your GitHub repository
   - Set build command: `./build.sh`
   - Set start command: `python -m gunicorn app:app`
   - Set environment: `Python 3`

3. **Configure Environment Variables**
   - Add all required environment variables listed above
   - Generate a strong SECRET_KEY (use `python -c "import secrets; print(secrets.token_hex(32))"`)

4. **Deploy**
   - Render will automatically deploy when you push to your main branch
   - The build.sh script will set up the database automatically

## Post-Deployment

1. **Access the System**
   - Use the developer credentials you set in environment variables
   - Login as developer to create school accounts

2. **Create School Accounts**
   - Go to "Manage Schools" in developer dashboard
   - Add new schools with their admin credentials
   - Set subscription types and payment status

## Database Management

- The system uses PostgreSQL in production with multi-tenant architecture
- Each school gets its own schema for data isolation
- Global tables (users, school configs, subscriptions) are in the public schema

## Security Features

- Multi-tenant data isolation
- Subscription-based access control
- Automatic school locking for expired subscriptions
- Encrypted sensitive data (when encryption is enabled)

## Monitoring

- Check Render logs for any deployment issues
- Monitor subscription status in the developer dashboard
- Use the "Check Subscriptions" button to auto-lock expired schools

## Support

For deployment issues, check:
1. Render build logs
2. Application logs in Render dashboard
3. Database connection status
4. Environment variables configuration