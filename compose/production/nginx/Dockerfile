FROM nginx:latest
COPY ./compose/production/nginx/local.conf /etc/nginx/conf.d/default.conf
COPY ./insights_integration_react_frontend/build/static /static/static
COPY ./staticfiles /static/static
