# 🚗 CarReview

**CarReview** é uma aplicação web interativa para entusiastas de automóveis, permitindo que usuários explorem, avaliem e discutam diversos modelos de carros.  
Utilizando **Firebase** para autenticação e banco de dados, a plataforma oferece uma experiência dinâmica e colaborativa.

---

## ✨ Funcionalidades
- ⭐ Avaliação de veículos com estrelas (1 a 5)  
- 🔐 Login com Google via Firebase Authentication  
- 💬 Chat em tempo real separado por modelo de carro  
- 🔎 Filtro por marcas e busca rápida  
- 📱 Layout moderno e responsivo (estilo WhatsApp no chat)  

---

## 🛠️ Tecnologias Utilizadas
- **HTML5, CSS3, JavaScript (ES6+)**  
- **Firebase** (Authentication + Firestore)  
- Estrutura modular com scripts:  
  - `auth.js` — Login e logout  
  - `rating_auth.js` — Sistema de avaliações  
  - `chat.js` + `chat-ui.js` — Lógica e interface do chat  

---

## 📁 Estrutura do Projeto
ProjectCarReview/ ├── index.html ├── style.css ├── /marca/ │ ├── audi.html │ ├── bmw.html │ └── ... ├── /static/ │ └── /images/ ├── /service/ │ ├── auth.js │ ├── rating_auth.js │ ├── chat.js │ └── chat-ui.js

---

## 🚀 Como Executar

### 1. Clone este repositório
```bash
git clone https://github.com/fabiolcalabrez/CarReview.git

2. Abra o projeto

Abra o arquivo index.html no navegador.

3. Configure seu Firebase

Authentication (método: Google)

Firestore Database

Insira as chaves no auth.js ou FirebaseService.js

💬 Chat Interativo

O chat funciona em três etapas:

Escolha da marca

Escolha do modelo

Envio de mensagens no chat do modelo

As mensagens são armazenadas no Firestore e visíveis para todos os usuários autenticados.

⭐ Sistema de Avaliação

Avaliações feitas apenas por usuários logados

Cada usuário pode avaliar uma única vez por carro

Avaliações salvas no Firestore

Exibe a média geral das avaliações

📄 Licença

Projeto acadêmico para fins educacionais.
Uso livre para estudo e demonstração.

🤝 Contribuições

Contribuições são bem-vindas!
Abra uma issue ou envie um pull request se quiser colaborar.
