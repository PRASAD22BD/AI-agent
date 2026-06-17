FROM n8nio/n8n:latest

USER root
# Install python if using a Debian-based image
RUN apt-get update && apt-get install -y python3 python3-pip || apk add --no-cache python3 py3-pip
RUN npm install -g n8n-nodes-base
USER node

# Use shell form for CMD to allow variable expansion and &&
CMD export N8N_PORT=${PORT:-10000} && n8n start
