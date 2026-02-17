# Loyalty Program Backend

## Project Structure

```
loyalty_program/
├── api/                    # API endpoints organized by user type
│   ├── admin/              # Admin panel endpoints
│   │   ├── routers/        # Admin-specific routes
│   │   └── services/       # Admin-specific business logic
│   ├── business_owner/     # Business owner panel endpoints
│   │   ├── routers/        # Business owner-specific routes
│   │   └── services/       # Business owner-specific business logic
│   ├── cashier/            # Cashier app endpoints
│   │   ├── routers/        # Cashier-specific routes
│   │   └── services/       # Cashier-specific business logic
│   └── frontend/           # Frontend/messenger endpoints
│       ├── routers/        # Frontend-specific routes
│       └── services/       # Frontend-specific business logic
├── repositories/          # Database access layer
├── schemas/               # Pydantic models for request/response validation
├── utils/                 # Utility functions
├── core/                  # Core application configuration and security
├── database/              # Database configuration and models
├── tests/                 # Test suite
│   ├── unit/              # Unit tests
│   ├── integration/       # Integration tests
│   └── e2e/               # End-to-end tests
├── config/                # Configuration files
├── models/                # SQLAlchemy models
├── main.py                # Application entry point
├── requirements.txt       # Dependencies
└── README.md              # This file
```

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up environment variables in `.env` file

3. Run the application:
   ```bash
   uvicorn main:app --reload
   ```