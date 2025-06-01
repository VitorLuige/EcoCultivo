// Comportamento modal confirmar saída
document.getElementById("btn-sair").addEventListener("click", function () {
  document.getElementById("modalSair").style.display = "grid";
});

document.getElementById("btn-cancelar").addEventListener("click", function () {
  document.getElementById("modalSair").style.display = "none";
});

document.getElementById("btn-confirmar").addEventListener("click", function () {
  window.location.href = "/login.html";
});