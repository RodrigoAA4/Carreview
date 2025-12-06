// static/auth.js
import { auth } from "./firebase.js";
import {
  GoogleAuthProvider,
  signInWithPopup,
  signOut,
  onAuthStateChanged
} from "https://www.gstatic.com/firebasejs/9.6.1/firebase-auth.js";

// Cria o provider do Google
const provider = new GoogleAuthProvider();

// Atualiza a interface com o estado do usuário logado/deslogado
function atualizarInterfaceUsuario(user) {
  const userInfo = document.getElementById("user-info");
  const loginBtn = document.getElementById("login-button");
  const logoutBtn = document.getElementById("logout-button");

  if (user) {
    userInfo.textContent = `OLÁ, ${user.displayName.toUpperCase()}!`;
    loginBtn.style.display = "none";
    logoutBtn.style.display = "block";
  } else {
    userInfo.textContent = "";
    loginBtn.style.display = "block";
    logoutBtn.style.display = "none";
  }
}

// Observa se o usuário já está logado ao carregar a página
onAuthStateChanged(auth, (user) => {
  atualizarInterfaceUsuario(user);
});

// Função para login com popup do Google
function signInWithGoogle() {
  signInWithPopup(auth, provider)
    .then((result) => {
      const user = result.user;
      atualizarInterfaceUsuario(user);
      Swal.fire({
        title: `Bem-vindo, ${user.displayName}!`,
        text: "Login realizado com sucesso.",
        icon: "success",
        confirmButtonText: "OK"
      });
    })
    .catch((error) => {
      console.error("Erro no login:", error);
      Swal.fire({
        title: "Erro ao logar",
        text: error.message,
        icon: "error"
      });
    });
}

// Função para logout
function signOutUser() {
  signOut(auth)
    .then(() => {
      atualizarInterfaceUsuario(null);
      Swal.fire({
        title: "Logout realizado",
        icon: "info",
        text: "Você saiu da sua conta."
      });
    })
    .catch((error) => {
      console.error("Erro no logout:", error);
      Swal.fire({
        title: "Erro ao deslogar",
        text: error.message,
        icon: "error"
      });
    });
}

// Conecta os botões ao carregamento da página
window.addEventListener("DOMContentLoaded", () => {
  const loginBtn = document.getElementById("login-button");
  const logoutBtn = document.getElementById("logout-button");

  if (loginBtn) loginBtn.addEventListener("click", signInWithGoogle);
  if (logoutBtn) logoutBtn.addEventListener("click", signOutUser);
});
