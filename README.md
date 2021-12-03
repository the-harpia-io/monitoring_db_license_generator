### Download Service
```
git clone https://github.com/the-harpia-io/monitoring_db_license_generator.git
```

### Prepare service to run
```
python -m pip install PyJWT==2.3.0
```

### How to generate License Key
```
python create_licenses.py --client Client_name --days_to_expire 30
```