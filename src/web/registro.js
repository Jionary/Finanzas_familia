const btnRegistro = document.getElementById("btn-registro");
btnRegistro.addEventListener("click", registro);

async function registro() {
  let establecimiento = document.getElementById("Input-establecimiento").value;
  let fecha = document.getElementById("Input-fecha-ticket").value;
  let concepto = document.getElementById("Input-concepto").value;
  let cantidad = document.getElementById("Input-cantidad").value;
  let precioUnitario = document.getElementById("Input-precio-unitario").value;
  let categoria = document.getElementById("Input-categoria").value;
  let dataToRegisterItems = {
    categoria_id: categoria,
    concepto: concepto,
    cantidad: cantidad,
    precio_unitario: precioUnitario,
  };
  let dataToRegisterTicket = {};
}
