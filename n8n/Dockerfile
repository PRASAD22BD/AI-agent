FROM n8nio/n8n:latest

USER root
RUN apk add --no-cache python3 py3-pip
RUN npm install -g n8n-nodes-base
USER node

# Render uses the PORT env var, n8n uses N8N_PORT
CMD ["export N8N_PORT=${PORT:-10000} && n8n start"]
