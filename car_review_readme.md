# 🚗 CarReview

**CarReview** é uma aplicação web interativa voltada para entusiastas e avaliadores do setor automotivo. A plataforma permite aos usuários **explorar marcas e modelos de carros, enviar avaliações com estrelas, e participar de um chat segmentado por modelo**, promovendo uma experiência comunitária e colaborativa.

> Este projeto foi desenvolvido como parte de um trabalho acadêmico e utiliza **Firebase** para autenticação e banco de dados em tempo real, além de tecnologias web modernas para um layout responsivo e intuitivo.

---

## ✨ Funcionalidades

- ⭐ **Avaliação de veículos** com sistema de notas de 1 a 5 estrelas  
- 🔐 **Login com Google** via Firebase Authentication  
- 💬 **Chat em tempo real**, segmentado por modelo de carro  
- 🔎 **Filtro por marcas** e interface de busca rápida  
- 📱 **Layout moderno e responsivo**, inspirado em mensageiros como WhatsApp  
- 📊 **Média das avaliações** exibida em tempo real  
- ↻ **Atualização dinâmica do frontend** sem recarregar a página  

---

## 🛠️ Tecnologias Utilizadas

- **Front-end:** HTML5, CSS3, JavaScript (ES6+)
- **Back-end:** Flask (Python)
- **Persistência:**  
  - Firebase Firestore (mensagens do chat)  
  - LocalStorage + JSON para sistema de avaliações (MVP)  
- **Bibliotecas e APIs:**  
  - Firebase Authentication  
  - TensorFlow.js + Universal Sentence Encoder (tentativa de IA no chat)  
- **Ferramentas:**  
  - Visual Studio Code  
  - Git e GitHub  
  - Chrome DevTools  
  - Postman / Thunder Client  

---

## 📁 Estrutura do Projeto

```
CarReview/
├── index.html
├── style.css
├── /marca/
│   ├── audi.html
│   ├── bmw.html
│   └── ...
├── /static/
│   └── /images/
├── /service/
│   ├── auth.js          # Autenticação (login/logout)
│   ├── rating_auth.js   # Avaliação com estrelas
│   ├── chat.js          # Lógica do chat
│   └── chat-ui.js       # Interface do chat
```

---

## 🚀 Como Executar Localmente

1. **Clone este repositório:**
```bash
git clone https://github.com/fabiolcalabrez/CarReview.git
```

2. **Abra o projeto em seu editor** e inicie o backend com Flask:
```bash
python -m venv .venv
.venv\Scripts\activate
pip install flask
python CarReview.py
# Acesse em: http://127.0.0.1:5000
```

3. **Configure seu Firebase:**
   - Ative o método de login com Google em **Authentication**
   - Crie uma coleção em **Firestore** para armazenar mensagens
   - Insira suas chaves de API no `auth.js` e `chat.js`

---

## 💬 Chat Interativo

O chat funciona em três etapas:
1. Escolha da marca  
2. Seleção do modelo  
3. Envio de mensagens no chat do modelo escolhido  

As mensagens são sincronizadas em tempo real com o **Firestore** e visíveis a todos os usuários autenticados.

---

## ⭐ Sistema de Avaliação

- Apenas usuários logados podem avaliar  
- Cada usuário avalia apenas **uma vez por modelo**  
- Avaliações salvas localmente e atualizadas em tempo real  
- A média é recalculada automaticamente após cada envio  

---

## 🤖 Tentativa de Integração com IA (POC)

Exploramos o uso do **TensorFlow.js** com o **Universal Sentence Encoder (USE)** para gerar respostas automáticas no chat. Apesar de configurado corretamente, o modelo não interpretava com precisão as mensagens enviadas, retornando múltiplas respostas desconexas. A integração não foi finalizada, mas serviu como uma importante prova de conceito para aprendizado em IA no navegador.

---

## 🧪 Testes Realizados

- Testes funcionais do sistema de avaliações  
- Testes do chat: envio, recepção e persistência local  
- Testes visuais: responsividade, contraste, layout  
- Testes de POC com TensorFlow.js (falho, porém documentado)  

---

## 📄 Licença

> Este é um **projeto acadêmico** desenvolvido exclusivamente para fins educacionais.  
> É permitido seu uso para estudo, demonstração ou extensão não-comercial.

---

## 🤝 Contribuições

Contribuições são **muito bem-vindas**!

Caso queira colaborar, abra uma **issue** ou envie um **pull request** com melhorias, sugestões ou correções.

