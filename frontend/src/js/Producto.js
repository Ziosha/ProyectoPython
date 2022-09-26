let rootGame =  document.getElementById('root'),
    homGame = document.getElementById('games')
    title = document.getElementById('title');


const rendergames = (i, t, d, p) => 
{   
    
    return `
    <div class="card text-white bg-dark dark" style="width: 18rem;">
    <img src="http://127.0.0.1:5500/frontend/images/${i}" height = "200em"  class="card-img-top" alt="...">
    <div class="card-body">
        <h5 class="card-title">${t}</h5>
        <p class="card-text">${d}</p>
        <p class="card-text">Precio: ${p}</p>
        <a href="#" class="btn btn-primary">Comprar</a>
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
                        const {Image, Nom_producto, Descripcion, Precio_producto} = element
                        rootGame.innerHTML += rendergames(Image, Nom_producto, Descripcion, Precio_producto)
                    });
                })
                .catch(error => console.log(error))
})






