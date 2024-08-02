from fastapi import FastAPI
from .routes import router

app = FastAPI()  # Create a new FastAPI application instance

app.include_router(router)  # Include the router in the application

# Entry point for running the application
if __name__ == "__main__":
    import uvicorn
    # Run the application on localhost at port 8000
    uvicorn.run(app, host="127.0.0.1", port=8000)
