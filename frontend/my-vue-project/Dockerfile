# Використовуємо Node.js
FROM node:18

WORKDIR /app

# Встановлюємо залежності
COPY package.json package-lock.json ./
RUN npm install

# Копіюємо код
COPY . .

EXPOSE 5173

# Запускаємо сервер
CMD ["npm", "run", "serve"]
