// static/rating.js
import { db, auth } from "./firebase.js";
import { onAuthStateChanged } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-auth.js";
import {
  collection,
  doc,
  getDoc,
  setDoc,
  getDocs,
  serverTimestamp
} from "https://www.gstatic.com/firebasejs/9.6.1/firebase-firestore.js";

document.addEventListener("DOMContentLoaded", () => {
  const containers = document.querySelectorAll(".rating-container");

  containers.forEach(container => {
    const modelo = container.dataset.modelo;
    const stars = container.querySelectorAll(".rating");
    const mediaSpan = container.querySelector(".media-estrela");
    const suaSpan = container.querySelector(".sua-estrela");

    let user = null;
    let notaUsuario = 0;

    const atualizarVisual = (nota) => {
      stars.forEach(star => {
        const val = parseInt(star.dataset.value);
        star.classList.toggle("selected", val <= nota);
      });
    };

    const carregarNotaUsuario = async (uid) => {
      const ref = doc(db, "avaliacoes", modelo, "usuarios", uid);
      const snap = await getDoc(ref);
      if (snap.exists()) {
        notaUsuario = snap.data().estrelas;
        if (suaSpan) {
          suaSpan.textContent = `| Sua nota: ${notaUsuario}`;
          suaSpan.style.display = "inline";
        }
        atualizarVisual(notaUsuario);
      }
    };

    const calcularMedia = async () => {
      try {
        const ref = collection(db, "avaliacoes", modelo, "usuarios");
        const snap = await getDocs(ref);
        let soma = 0;
        let total = 0;

        snap.forEach(doc => {
          const dados = doc.data();
          if (typeof dados.estrelas === "number") {
            soma += dados.estrelas;
            total++;
          }
        });

        const media = total > 0 ? (soma / total).toFixed(1) : "0.0";
        if (mediaSpan) {
          mediaSpan.textContent = `Média: ${media}`;
          mediaSpan.style.display = "inline";
          mediaSpan.style.color = "#E63946";
        }
      } catch (e) {
        console.error(`Erro ao calcular média para ${modelo}:`, e);
        if (mediaSpan) {
          mediaSpan.textContent = `Média: erro`;
          mediaSpan.style.color = "#E63946";
        }
      }
    };

    onAuthStateChanged(auth, async (u) => {
      try {
        user = u;
        if (user) {
          await carregarNotaUsuario(user.uid);
        } else {
          if (suaSpan) suaSpan.style.display = "none";
        }
        await calcularMedia();
      } catch (erro) {
        console.error("Erro geral:", erro);
        if (mediaSpan) {
          mediaSpan.textContent = "Média: erro";
          mediaSpan.style.color = "#E63946";
        }
      }
    });

    stars.forEach(star => {
      star.addEventListener("click", async () => {
        if (!user) {
          alert("Faça login para avaliar.");
          return;
        }

        const valor = parseInt(star.dataset.value);
        await setDoc(doc(db, "avaliacoes", modelo, "usuarios", user.uid), {
          estrelas: valor,
          nomeUsuario: user.displayName || "Anônimo",
          timestamp: serverTimestamp()
        });

        notaUsuario = valor;
        if (suaSpan) {
          suaSpan.textContent = `| Sua nota: ${valor}`;
          suaSpan.style.display = "inline";
        }
        atualizarVisual(valor);
        await calcularMedia();
      });

      star.addEventListener("mouseenter", () => {
        const val = parseInt(star.dataset.value);
        stars.forEach(s => {
          s.classList.toggle("hovered", parseInt(s.dataset.value) <= val);
        });
      });

      star.addEventListener("mouseleave", () => {
        stars.forEach(s => s.classList.remove("hovered"));
        atualizarVisual(notaUsuario);
      });
    });
  });
});
