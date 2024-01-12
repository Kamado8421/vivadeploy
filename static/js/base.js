function toggleMenuResp() {
    var menu_resp = document.querySelector('.menu-resp');

    if (menu_resp.classList.contains('close')) {
        menu_resp.classList.remove('close');
    } else {
        menu_resp.classList.add('close');
    }
}


function goProfile(){
    location.href = '/teste'
}

function toGo(id){
    switch (id) {
        case 1:
        location.href = "{% url 'my_home' %}"
            break;
        case 2:
        location.href = 'profkkkile.html'
            break;
        case 3:
        location.href = 'galery_virtual.html'
            break;
        case 4:
        location.href = 'chat.html'
            break;
        case 5:
        location.href = 'search.html'
            break;
        case 6:
        location.href = 'event.html'
            break;
        case 7:
        location.href = 'collaborative_arte.html'
            break;
        case 8:
        location.href = '/support' 
            break;
    
        default:
            break;
    }
}

function toggleMenu() {
    const menu = document.querySelector('.menu');
    const main = document.querySelector('main');
    const links = document.querySelectorAll('.link');
    const support_link = document.querySelector('.support-link');

    // Adiciona ou remove a classe 'closed' no menu e ajusta o padding-left do main
    menu.classList.toggle('closed');
    main.style.paddingLeft = menu.classList.contains('closed') ? '75px' : '260px';

    let menu_closed = menu.classList.contains('closed');

    if(menu_closed){
        menu.style.width = '45px';
        links.forEach(link => {
            link.style.display = 'none';
        });
        support_link.style.display = 'none';
    } else {
        menu.style.width = '230px';
        links.forEach(link => {
            link.style.display = 'flex';
        });
        support_link.style.display = 'flex';
    }
}

function toGoEvents(){
    var content = document.getElementById('content-main');
    var content02 = document.getElementById('content-new-event');
    var content03 = document.getElementById('content-my-events');
    
    content02.style.display = 'none';
    content03.style.display = 'none';

    content.style.display = 'flex';
    content.style.flexDirection = 'column';
}

function toGoCreateEvents(){
    var content = document.getElementById('content-main');
    var content02 = document.getElementById('content-new-event');
    var content03 = document.getElementById('content-my-events');

    content.style.display = 'none';
    content03.style.display = 'none';

    content02.style.display = 'flex';
    content02.style.flexDirection = 'column';
}

function toShowMyEvents(){
    var content = document.getElementById('content-main');
    var content02 = document.getElementById('content-new-event');
    var content03 = document.getElementById('content-my-events');

    content.style.display = 'none';
    content02.style.display = 'none';

    content03.style.display = 'flex';
    content03.style.flexDirection = 'column';
}