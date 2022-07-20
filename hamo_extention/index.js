setInterval(() => {
    let imgs = document.querySelectorAll('img');
    imgs.forEach((a, i) => {
        a.src = "https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjA1MzFfMjU0%2FMDAxNjUzOTc0NTM5NTEw.UdcA8_cWQ7KIdh_8HnUvpCjsZpCsg9mseJYLF-Kjz98g.mR_I2mVe8V1r9aXJz5D7hqEhT9PZuEvhd2n45Ipeqp4g.GIF.thejinjucity%2Femot_001_x3_5.gif&type=sc960_832_gif"
    })
    
}, 500)


document.querySelectorAll('*').forEach((el)=>{
    const checkBgImage = getComputedStyle(el).backgroundImage !== "none";
    if(checkBgImage){
         el.style.backgroundImage='url("https://search.pstatic.net/common/?src=http%3A%2F%2Fimgnews.naver.net%2Fimage%2F5372%2F2022%2F01%2F07%2F0000088166_004_20220114150604769.jpg&type=sc960_832")';
     }
   })
   