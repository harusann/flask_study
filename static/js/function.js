const request = async (url, headers, options) => {
    if (!options) {
        options = {}
    }
    const OPTION = {
        method:'POST',
        headers:headers,
        body:JSON.stringify(options)
    }
    const res = await fetch(url, OPTION);
    return res.json();
}

const jsonGet = async (url) => {
    const res = await fetch(url);
    return res.json();
}

const onSignIn = async (googleUser) => {
    const URL = 'http://localhost:8000/'
    const header = {
        'Content-Type':'application/x-www-form-urlencoded'
    }
    let id_token = googleUser.getAuthResponse().id_token;
    xhr.send('idtoken=' + id_token);

    await request(URL, header, )
}