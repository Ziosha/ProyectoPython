let rootGame =  document.getElementById('root'),
    homGame = document.getElementById('games')
    title = document.getElementById('title');


const rendergames = (i, t, d, p, cod) => 
{   
    
    return `
    <div class="card text-white bg-dark dark" style="width: 18rem;">
    <img src="http://127.0.0.1:5500/frontend/images/${i}" height = "200em"  class="card-img-top" alt="...">
    <div class="card-body">
        <h5 class="card-title">${t}</h5>
        <p class="card-text">${d}</p>
        <p class="card-text">Precio: ${p}</p>
        <a href="#" class="btn btn-primary" onclick="comprar(${cod})">Comprar</a>
    </div>
    </div>
    `
}

homGame.addEventListener('click',()=> {
        const game = fetch('http://127.0.0.1:3000/producto')
        game.then(res => res.json())
                .then(data => {
                    rootGame.innerHTML = null;
                    title.innerHTML = "JUEGOS"
                    data.forEach(element => {
                        const {Image, Nom_producto, Descripcion, Precio_producto, Cod_producto} = element
                        rootGame.innerHTML += rendergames(Image, Nom_producto, Descripcion, Precio_producto, Cod_producto)
                    });
                })
                .catch(error => console.log(error))
})



const comprar =(c) =>
{
    var datos = {
        Cod_producto : c,
        ID_usuario : 2
    }
    const comprar = fetch(`http://localhost:3000/compra`,{
        method: 'POST',
        body : JSON.stringify(datos),
        headers : {'Content-Type': 'application/json'}
      })
      comprar.then(resp => resp.json())
              .then(data => {
                  if(data.statusCode = 200)
                  {
                    alert("Producto Comprado")
                  }
                  else{
                    alert("Producto no modificado")
                  }
              })
              .catch(error => console.log(error))
}



