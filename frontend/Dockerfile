FROM node:18.16.0

WORKDIR /web

COPY package.json package-lock.json ./

RUN npm install

COPY . .

CMD ["npm", "run", "dev"] 
