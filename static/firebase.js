// static/firebase.js
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-app.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-firestore.js";
import { getAuth } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-auth.js";

// 🔐 Copie isso do seu Firebase > Configurações do projeto > Configuração do SDK
const firebaseConfig = {
  apiKey: "AIzaSyCCoKD-_GdqkSzwrAk9kLg191ra1oN19uo",
  authDomain: "carreview-6c9d7.firebaseapp.com",
  projectId: "carreview-6c9d7",
  storageBucket: "carreview-6c9d7.appspot.com",
  messagingSenderId: "585266517662",
  appId: "1:585266517662:web:4a76d501b406f1dfb38d8f"
};

// Inicialização
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);
const auth = getAuth(app);

export { db, auth };
