let rootUser = document.getElementById('root'),
    user = document.getElementById('user'),
    titleUSer = document.getElementById('title');

const renderUser = (i,n,ap,am,p,c,t) =>
{
    return `
    
      <tr>
        <th scope="row">${i}</th>
        <td>${n}</td>
        <td>${ap}</td>
        <td>${am}</td>
        <td>${p}</td>
        <td>${c}</td>
        <td>${t}</td>
      </tr>  
    `
}


user.addEventListener('click', () => {
    
    rootUser.innerHTML = null
    rootUser.innerHTML = ` 
    <table class="table table-dark">
    <thead>
      <tr>
        <th scope="col">#</th>
        <th scope="col">Nombre</th>
        <th scope="col">Apellido Paterno</th>
        <th scope="col">Apellido Materno</th>
        <th scope="col">Pais</th>
        <th scope="col">Correo</th>
        <th scope="col">Telefono</th>
      </tr>
    </thead>
    <tbody id="tablebody">
    </tbody>
    </table>
    `

    let table = document.getElementById('tablebody')

    const users = fetch('http://127.0.0.1:3000/usuario')
        users.then(res => res.json())
                .then(data => {
                    table.innerHTML = null;
                    title.innerHTML = "USUARIOS"
                    data.forEach(element => {
                        const {ID_usuario, Nombre_usuario, Apellido_Paterno, Apellido_Materno, Pais, Correo, Telefono} = element
                        table.innerHTML += renderUser(ID_usuario, Nombre_usuario, Apellido_Paterno, Apellido_Materno, Pais, Correo, Telefono)
                    });
                })
                .catch(error => console.log(error))

    
})