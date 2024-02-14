# Build Stage for Frontend
FROM node:latest as frontend-build

WORKDIR /app

# Copy package*.json from the front_end/bot_vue directory
COPY front_end/bot_vue/package*.json ./

RUN npm install

# Copy the entire front-end code
COPY front_end/bot_vue/ .

RUN npm run build

# Backend Build Stage
FROM python:3.8 as backend-build

WORKDIR /app

# Copy the backend code
COPY back_end/ .

# Copy the requirements file from the back_end directory
COPY back_end/requirements.txt .

# Install backend dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your Flask app will run on
EXPOSE 5000

# Command to start the Flask application
CMD ["python", "app.py"]

# Production Stage (Nginx)
FROM nginx

# Create a directory for the application in the nginx container
RUN mkdir /app

# Copy the frontend build output from the frontend-build stage to the /app directory in the nginx container
COPY --from=frontend-build /app/dist /app

# Copy the nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Expose the port your Nginx server will run on
EXPOSE 80

# Command to start Nginx
CMD ["nginx", "-g", "daemon off;"]

