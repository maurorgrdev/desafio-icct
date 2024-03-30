# Use uma imagem base que inclua o Node.js
FROM node:18

# Defina o diretório de trabalho
WORKDIR /frontend

# Copie apenas os arquivos necessários para o diretório de trabalho
COPY package.json yarn.lock ./

# Instale as dependências do projeto
RUN yarn install

# Copie o restante dos arquivos do projeto para o diretório de trabalho
COPY . .

# Execute o comando de construção para compilar o código frontend
RUN yarn build

# Expor a porta utilizada pelo servidor de desenvolvimento do Quasar
EXPOSE 9000

# Comando para iniciar o servidor de desenvolvimento do Quasar
CMD ["yarn", "quasar", "dev"]
