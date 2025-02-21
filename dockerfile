FROM nginx
COPY react2.html /usr/share/nginx/html
RUN docker build -t react-image .

