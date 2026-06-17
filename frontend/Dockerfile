FROM node:20-slim AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM node:20-slim AS runner
WORKDIR /app
ENV NODE_ENV=production
ENV PORT=3000
ENV HOSTNAME="0.0.0.0"

# Copy essential files, allowing for missing public folder if necessary
COPY --from=builder /app/next.config.mjs ./
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json ./package.json
# Use a wildcard to copy public only if it exists
COPY --from=builder /app/public* ./public/

EXPOSE 3000
CMD ["sh", "-c", "npm start -- -p ${PORT:-3000}"]
