let addgame = document.getElementById('addgames'),
    rootAddgame = document.getElementById('root')


addgame.addEventListener('click', () =>{
    rootAddgame.innerHTML = null
    rootAddgame.innerHTML = `
    <div class="form">
    <h1 style="text-align: center">Registrar Juego</h1>
      <input type="text" name="nombre" placeholder="Nombres" size="40" id="nom" required/>
      <input type="text" name="apellidoP" placeholder="Precio" size="40" id="ap" required/>
      <input type="text" name="apellidoM" placeholder="Descripcion" size="40" id="am" required/>
      <input type="date" name="pais" placeholder="Fecha Lanzamiento" size="40" id="pais" required/>
      <input type="number" name="telefono" placeholder="Categoria" size="40" id="phone" required/>
      <input type="reset" value="Enviar" id="send" />
  </div>
    `
    let nom = document.getElementById('nom'),
        ap = document.getElementById('ap'),
        am = document.getElementById('am'),
        pais = document.getElementById('pais'),
        send = document.getElementById('send')

    send.addEventListener('click', () => {
        var data = {
            Nom_producto: nom.value,
            Precio_producto : ap.value,
            Descripcion : am.value,
            Fecha_lanzamiento : pais.value,
            Cod_categoria: phone.value,
            Image : "game.jpg" 
          }                
            
          const addUsers = fetch("http://localhost:3000/producto",{
                  method : 'POST',
                  body:  JSON.stringify(data),
                  headers:{'Content-Type': 'application/json'}
              })
              addUsers.then(res => res.json())
                      .then(data => {
                          if(data.statusCode = 200)
                          {
                              alert("Producto registrado")
                          }
                          else {alert("error al registrar producto")}
          
                      })
                      .catch(error => console.log(error))

    })
        



} )