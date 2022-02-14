const hamburger = document.querySelector(".hamburger-image");
const navLinks = document.querySelector(".hamburger-resp");
const hamburgerListClose = document.querySelector(".exit-hamburger-list");

hamburgerListClose.addEventListener("click", () => {
  navLinks.classList.remove("open");
});

hamburger.addEventListener("click", () => {
  navLinks.classList.toggle("open");
});

let screenWidth = screen.availWidth;

const showFoto = () => {
    const fotoBox = document.querySelectorAll(".statistics-down-container-box");
    const statisticsBox = document.querySelectorAll(".statistics-main-image");
    //Foto from list statistics
    statisticsBox.forEach((statImage) => {
        statImage.addEventListener("click", function (){
            const staticImgContainer = document.createElement("div");
            const staticImg = document.createElement("div");
            staticImg.classList.add("static-image");
            staticImgContainer.classList.add("static-image-container");
            staticImgContainer.appendChild(staticImg);
            staticImg.innerHTML = statImage.innerHTML;
            document.body.appendChild(staticImgContainer);
            staticImgContainer.addEventListener("click", function () {
              staticImgContainer.remove(staticImgContainer);
            });
        });
    });

    //Foto from main html
    fotoBox.forEach((fotoStatic) => {
      fotoStatic.addEventListener("click", function () {
        const staticImgContainer = document.createElement("div");
        const staticImg = document.createElement("div");
        staticImg.classList.add("static-image");
        staticImgContainer.classList.add("static-image-container");
        staticImgContainer.appendChild(staticImg);
        staticImg.innerHTML = fotoStatic.innerHTML;
        document.body.appendChild(staticImgContainer);
        staticImgContainer.addEventListener("click", function () {
          staticImgContainer.remove(staticImgContainer);
        });
      });
    });

    //Foto from post details
    const detailImage = document.querySelectorAll(".post-details-image img");
    detailImage.forEach((postImage) => {
        postImage.addEventListener("click", function(){
            const staticImgContainer = document.createElement("div");
            const staticImg = document.createElement("div");
            const postImageWidth = postImage.naturalWidth;
            const postImageHeight = postImage.naturalHeight;
            const posImageImg = postImage.parentNode;
            const result = postImageWidth/postImageHeight;
            console.log(result);
            if(result < 1){
                staticImg.classList.add("static-height-image");
            }
            else{
                staticImg.classList.add("static-image");
            }
            staticImgContainer.classList.add("static-image-container");
            staticImg.innerHTML = posImageImg.innerHTML;
            staticImgContainer.appendChild(staticImg);
            document.body.appendChild(staticImgContainer);
            staticImgContainer.addEventListener("click", function () {
              staticImgContainer.remove(staticImgContainer);
            });
        });
    });
};

let currentDate = new Date();
let currentYear = currentDate.getFullYear();


const footerInfo = document.querySelector(".contact-footer h3")
footerInfo.innerHTML = "Ratownicy Medyczni Leszno &copy " + currentYear;

showFoto();