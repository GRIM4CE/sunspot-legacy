from app import create_app

app = create_app()

if __name__ == '__main__':
    # Use host='0.0.0.0' to make the app accessible externally 
    app.run(host='0.0.0.0', port=3000, debug=False)