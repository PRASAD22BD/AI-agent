FROM n8nio/n8n:latest-debian

USER root
RUN apt-get update && apt-get install -y python3 python3-pip
RUN npm install -g n8n-nodes-base
USER node

# Render uses the PORT env var, n8n uses N8N_PORT
CMD ["sh", "-c", "export N8N_PORT=${PORT:-10000} && n8n start"]
