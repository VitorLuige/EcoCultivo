/* olho-mágico */
document.querySelectorAll(".toggle-password").forEach((btn) => {
  btn.addEventListener("mousedown", () => {
    const targetInput = document.getElementById(btn.dataset.target);
    if (targetInput) {
      targetInput.type = "text";
      btn.src = "/assets/imgs/eye.svg";
    }
  });

  btn.addEventListener("mouseup", () => {
    const targetInput = document.getElementById(btn.dataset.target);
    if (targetInput) {
      targetInput.type = "password";
      btn.src = "/assets/imgs/eye-off.svg";
    }
  });

  btn.addEventListener("mouseleave", () => {
    const targetInput = document.getElementById(btn.dataset.target);
    if (targetInput) {
      targetInput.type = "password";
      btn.src = "/assets/imgs/eye-off.svg";
    }
  });
});

/* Validação de senha */
const formCadastro = document.getElementById("formCadastro");

if (formCadastro) {
  formCadastro.addEventListener("submit", function (e) {
    const senha = document.getElementById("senha").value;
    const confirmarSenha = document.getElementById("confirmarSenha").value;
    const erro = document.getElementById("erro-senha");

    if (senha !== confirmarSenha) {
      e.preventDefault();
      erro.style.display = "block";
    } else {
      erro.style.display = "none";
    }
  });
}
