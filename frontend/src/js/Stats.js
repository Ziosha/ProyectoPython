let rootStat = document.getElementById('root'),
    stats = document.getElementById('stats'),
    titleStat = document.getElementById('title');

const renderStats = (i,n,ap,am,p,c,t) =>
{
    return `
    
      <tr>
        <th scope="row">${i}</th>
        <td>${n}</td>
        <td>${ap}</td>
        <td>${am}</td>
        <td>${p}</td>
      </tr>  
    `
}


stats.addEventListener('click', () => {
    
    rootStat.innerHTML = null
    rootStat.innerHTML = ` 
    <table class="table table-dark">
    <thead>
      <tr>
        <th scope="col">#</th>
        <th scope="col">Cliente</th>
        <th scope="col">Producto</th>
        <th scope="col">Precio</th>
        <th scope="col">Fecha</th>
      </tr>
    </thead>
    <tbody id="tablebody">
    </tbody>
    </table>
    `

    let tables = document.getElementById('tablebody')

    const stat = fetch('http://localhost:3000/reporte')
        stat.then(res => res.json())
                .then(data => {
                    tables.innerHTML = null;
                    titleStat.innerHTML = "REPORTE"
                    data.forEach(element => {
                        const {ID_compra, Nombre, Nom_producto, Precio_producto, CreationDate} = element
                        tables.innerHTML += renderStats(ID_compra, Nombre, Nom_producto, Precio_producto, CreationDate)
                    });
                })
                .catch(error => console.log(error))

    
})