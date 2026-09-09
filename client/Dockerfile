# Use a clean, tiny web server image
FROM nginx:alpine

COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy your locally compiled dist folder straight into the web root folder
COPY dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]