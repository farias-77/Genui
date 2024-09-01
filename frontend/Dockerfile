# Use an official Node.js image as the base
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Use Nginx to serve the app
FROM nginx:alpine

# Copy build files
COPY --from=0 /app/build /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
