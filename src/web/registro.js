const btnRegistro = document.getElementById("btn-registro");
btnRegistro.addEventListener("click", registro);
const btnAddItem = document.querySelector(".btn-agg-item");
btnAddItem.addEventListener("click", addDivToRegisterItem);
const contenedor = document.getElementById("Contenedor-items");
contenedor.addEventListener("click", function (event) {
  if (event.target.classList.contains("btn-borrar-item")) {
    event.target.closest(".Fila-items").remove();
  }
});
let opcionesGlobales = "";

async function registro() {
  const rutaApiPostTicket = `http://localhost:8000/api/v1/tickets`;
  let establecimiento = document.getElementById("Input-establecimiento").value;
  let fecha = document.getElementById("Input-fecha-ticket").value;
  let notas = document.getElementById("Input-notas").value;
  let itemsExtracted = document.querySelectorAll(".Fila-items");
  let itemsArray = [];
  for (let item of itemsExtracted) {
    let concepto = item.querySelector(".Input-concepto").value;
    let cantidad = parseInt(item.querySelector(".Input-cantidad").value);
    let precioUnitario = parseFloat(
      item.querySelector(".Input-precio-unitario").value
    );
    let categoria = parseInt(item.querySelector(".Input-categoria").value);
    let itemToAdd = {
      categoria_id: categoria,
      concepto: concepto,
      cantidad: cantidad,
      precio_unitario: precioUnitario,
    };
    itemsArray.push(itemToAdd);
  }

  let dataToRegisterTicket = {
    establecimiento: establecimiento,
    fecha: fecha,
    notas: notas,
    items: itemsArray,
  };
  console.log(dataToRegisterTicket);
}

function addDivToRegisterItem() {
  contenedor.insertAdjacentHTML(
    "beforeend",
    `<div class="Fila-items flex flex-col gap-4 p-4 max-w-2xl mx-auto">
          <input
            type="text"
            name="Concepto"
            placeholder="Ingrese el concepto"
            class="Input-concepto border border-gray-300 rounded px-3 py-2 w-full focus:outline-blue-500"
          />
          <input
            type="number"
            name="Cantidad"
            placeholder="Ingrese la cantidad"
            class="Input-cantidad border border-gray-300 rounded px-3 py-2 w-full focus:outline-blue-500"
          />
          <input
            type="number"
            name="Precio_unitario"
            placeholder="Ingrese el precio unitario"
            class="Input-precio-unitario border border-gray-300 rounded px-3 py-2 w-full focus:outline-blue-500"
          />
          <select
            type="number"
            name="Categoria"
            placeholder="Ingrese la categoria"
            class="Input-categoria border border-gray-300 rounded px-3 py-2 w-full focus:outline-blue-500"
          >${opcionesGlobales}</select>
          <button
            class="btn-borrar-item bg-blue-600 text-white font-bold py-2 px-4 rounded hover:bg-blue-700"
          >
            Borrar item
          </button>
        </div>`
  );
}

async function drawCategories() {
  rutaApiCategorias = `http://localhost:8000/api/v1/categorias`;
  let dataCategorias = await fetch(rutaApiCategorias);
  let dataJsonCategorias = await dataCategorias.json();
  console.log(dataJsonCategorias);
  for (let categoria of dataJsonCategorias["Tus categorias son: "]) {
    opcionesGlobales += `<option value="${categoria.id}">${categoria.nombre}</option>`;
  }
  document.querySelector(".Input-categoria").innerHTML = opcionesGlobales;
}
drawCategories();
