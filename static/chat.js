// static/chat.js
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-app.js";
import {
  getFirestore,
  collection,
  addDoc,
  onSnapshot,
  query,
  orderBy
} from "https://www.gstatic.com/firebasejs/9.6.1/firebase-firestore.js";
import {
  getAuth,
  onAuthStateChanged
} from "https://www.gstatic.com/firebasejs/9.6.1/firebase-auth.js";

const firebaseConfig = {
  apiKey: "AIzaSyCCoKD-_GdqkSzwrAk9kLg191ra1oN19uo",
  authDomain: "carreview-6c9d7.firebaseapp.com",
  projectId: "carreview-6c9d7",
  storageBucket: "carreview-6c9d7.appspot.com",
  messagingSenderId: "585266517662",
  appId: "1:585266517662:web:4a76d501b406f1dfb38d8f"
};

const app = initializeApp(firebaseConfig);
const db = getFirestore(app);
const auth = getAuth(app);

let currentUid = null;
onAuthStateChanged(auth, (user) => {
  currentUid = user ? user.uid : null;
});

const marcas = {
  "Audi": ["A3", "Q5", "RS5"],
  "BMW": ["320i", "X1", "X6"],
  "Chevrolet": ["Onix", "Tracker", "S10"],
  "Citroën": ["C3", "DS4", "C3 Picasso"],
  "Fiat": ["Argo", "Cronos", "Toro"],
  "Ford": ["Ka", "Ranger", "Mustang"],
  "Honda": ["Civic", "HR-V", "Fit"],
  "Hyundai": ["HB20", "Creta", "Tucson"],
  "Jaguar": ["XF", "F-Pace", "f-type"],
  "Jeep": ["Renegade", "Compass", "Wrangler"],
  "Land Rover": ["Evoque", "Discovery", "Defender"],
  "Mercedes Benz": ["Classe A", "GLA", "GLE"],
  "Mitsubishi": ["lancer", "triton", "pajero"],
  "Nissan": ["Kicks", "Sentra", "Frontier"],
  "Peugeot": ["208", "2008", "3008"],
  "Porsche": ["Macan", "Cayenne", "911"],
  "Toyota": ["Corolla", "Corolla Cross", "Hilux"],
  "Volkswagen": ["Polo", "T-Cross", "Amarok"]
};

function preencherMarcas() {
  const cont = document.getElementById("chat-marcas");
  if (!cont) return;
  cont.innerHTML = "";
  Object.keys(marcas).forEach((marca) => {
    const btn = document.createElement("button");
    btn.className = "chat-brand-btn";
    btn.textContent = marca;
    btn.addEventListener("click", () => mostrarModelos(marca));
    cont.appendChild(btn);
  });
}

window.mostrarModelos = function (marca) {
  const modelosDiv = document.getElementById("modelos-lista");
  const modelos = marcas[marca];

  document.getElementById("chat-marcas").style.display = "none";
  document.getElementById("chat-modelos").style.display = "flex";
  modelosDiv.innerHTML = "";

  modelos.forEach((m) => {
    const btn = document.createElement("button");
    btn.className = "chat-model-btn";
    btn.textContent = m;
    btn.onclick = () => abrirChatModelo(marca, m);
    modelosDiv.appendChild(btn);
  });
};

window.voltarMarcas = function () {
  document.getElementById("chat-modelos").style.display = "none";
  document.getElementById("chat-marcas").style.display = "flex";
};

window.toggleChat = function () {
  const chatBox = document.getElementById("chat-box");
  const isHidden = chatBox.style.display === "none" || getComputedStyle(chatBox).display === "none";

  if (isHidden) {
    chatBox.style.display = "flex";
    chatBox.classList.add("expanded");
    document.getElementById("chat-content").innerHTML = `
      <div id="chat-marcas" class="chat-marcas"></div>
      <div id="chat-modelos" class="chat-modelos" style="display:none;">
        <button onclick="voltarMarcas()" class="back-btn">⬅ Voltar</button>
        <div id="modelos-lista"></div>
      </div>
    `;
    preencherMarcas();
  } else {
    chatBox.style.display = "none";
    chatBox.classList.remove("expanded");
  }
};

window.abrirChatModelo = async (marca, modelo) => {
  const container = document.getElementById("chat-content");
  const chatBox = document.getElementById("chat-box");
  const chatId = `${marca}_${modelo}`;

  chatBox.classList.add("expanded");

document.getElementById("chat-marcas").style.display = "none";
document.getElementById("chat-modelos").style.display = "none";

container.innerHTML = `
  <div id="chat-header" class="chat-header">
    <div class="chat-header-left">
      <button class="back-btn">⬅ Voltar</button>
      <strong style="margin-left: 10px;">Chat ${marca} ${modelo}</strong>
    </div>
  </div>
  <div id="chat-messages" style="flex:1; overflow-y:auto; padding:10px;"></div>
`;

const backBtn = container.querySelector(".back-btn");
backBtn.addEventListener("click", () => {
  document.getElementById("chat-content").innerHTML = `
    <div id="chat-marcas" class="chat-marcas"></div>
    <div id="chat-modelos" class="chat-modelos" style="display:none;">
      <button onclick="voltarMarcas()" class="back-btn">⬅ Voltar</button>
      <div id="modelos-lista"></div>
    </div>
  `;
  preencherMarcas();
});



  const chatRef = collection(db, "chats", chatId, "mensagens");
  const q = query(chatRef, orderBy("timestamp"));

  onSnapshot(q, (snapshot) => {
    const chatBox = document.getElementById("chat-messages");
    snapshot.docChanges().forEach(change => {
      if (change.type === "added") {
        const msg = change.doc.data();
        const msgDiv = document.createElement("div");
        msgDiv.classList.add("msg");
        const isMine = auth.currentUser && msg.uid === auth.currentUser.uid;
        msgDiv.classList.add(isMine ? "direita" : "esquerda");
        msgDiv.innerHTML = `<strong>${msg.nome}</strong><br>${msg.texto}`;
        chatBox.appendChild(msgDiv);
      }
    });
    chatBox.scrollTop = chatBox.scrollHeight;
  });

  document.getElementById("send-btn").onclick = async () => {
    const input = document.getElementById("chat-input");
    const texto = input.value.trim();
    const user = auth.currentUser;

    if (!user) {
      alert("Você precisa estar logado para comentar.");
      return;
    }

    if (texto === "") return;

    await addDoc(chatRef, {
      texto,
      nome: user.displayName,
      uid: user.uid,
      timestamp: new Date()
    });

    input.value = "";
  };
};



