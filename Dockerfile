FROM nginx:alpine

# Kopiere alle HTML-Dateien
COPY *.html /usr/share/nginx/html/
COPY *.jpg /usr/share/nginx/html/
COPY *.css /usr/share/nginx/html/
COPY *.js /usr/share/nginx/html/

# Kopiere nginx-Konfiguration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Exponiere Port 80
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
