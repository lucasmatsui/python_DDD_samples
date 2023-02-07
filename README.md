 # DDD samples with Python
This project follow the main DDD tatical concepts:
- Application Layer
- Domain Layer
- Infrastructure Layer

### Folder Structure
To build this representation of folder structure, it was following the moduralization concepts showing in DDD book
```
├── application
│   └── user
│       └── create_user
│           ├── create_user.py
│           ├── create_user_input.py
│           └── create_user_output.py
├── domain
│   └── model
│       └── user
│           ├── email.py
│           ├── invalid_email_error.py
│           ├── user.py
│           └── user_repository.py
├── infra
│   ├── repositories
│   │   ├── in_memory_user_repository.py
│   │   └── mysql_user_repository.py
│   └── utils
│       └── response_error.py
└── ui
    └── controllers
        └── user_controller.py
├── __init__.py
├── main.py

```

## License

[MIT](https://choosealicense.com/licenses/mit/)
