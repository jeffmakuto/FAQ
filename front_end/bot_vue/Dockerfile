# Build Stage for Frontend
FROM node:latest as frontend-build

WORKDIR /app

# Copy package*.json from the front_end/bot_vue directory
COPY package*.json ./

RUN npm install

# Copy the entire front-end code
COPY . .

RUN npm run build

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

