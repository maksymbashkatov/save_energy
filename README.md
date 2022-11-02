# JWT authentication
Go to Postman;

Create method POST page (http://127.0.0.1:8000/auth/token/login), Body -> form-data -> enter existing data for authorization (email and password) -> send;

Copy and save auth_token;

Create method GET (or other) page (http://127.0.0.1:8000/datapoints/4);

Headers -> create Authorization header and paste token (example: Token ba4455070c7692f20573da69597a1a48783c1107) -> send.

---

# Database data initialization

Go to py manage.py shell;

Run data_initialization func from core.data_ini.