from setuptools import setup, find_packages

setup(
    name="smartfee",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask==3.0.3',
        'Flask-SQLAlchemy==3.1.1',
        'Flask-Login==0.6.3',
        'Flask-WTF==1.2.1',
        'Werkzeug==3.0.4',
        'Jinja2==3.1.4',
        'MarkupSafe==2.1.5',
        'python-dotenv==1.0.1',
        'gunicorn==21.2.0',
        'psycopg2-binary>=2.9.9,<3.0.0',
        'cryptography>=41.0.0',
        'whitenoise==6.6.0',
        'email-validator==2.1.0.post1',
        'python-dateutil==2.8.2',
        'pytz==2024.1',
        'itsdangerous==2.2.0',
        'blinker==1.8.2',
        'WTForms==3.1.2'
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'smartfee=wsgi:application',
        ],
    },
)
