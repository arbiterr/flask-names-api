from config import connex_app


# Read the swagger.yml file to configure the endpoints
connex_app.add_api("swagger.yml")

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    connex_app.run(host='0.0.0.0', port=5000, debug=True)
