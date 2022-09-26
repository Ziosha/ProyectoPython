let homes = document.getElementById('home'),
    rootHome = document.getElementById('root'),
    titleHome = document.getElementById('title');


const renderhome = () => 
{
    return `
        <div class="banner">
        <header>
        <h1>Games Store</h1>
        </header>
    </div>
    `
}


homes.addEventListener('click', () => {
    rootHome.innerHTML = null
    titleHome.innerHTML = null
    rootHome.innerHTML = renderhome()
})

titleHome.innerHTML = null
rootHome.innerHTML = null
rootHome.innerHTML = renderhome()

