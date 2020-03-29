// document.getElementById('button-custom').addEventListener('click',fuction(){
//     document.querySelector('.bg-modal-jp').style.display = 'flex';
// });

// document.querySelector('.button-wrap-lg').addEventListener('click',function(){
//     document.querySelector('.bg-modal-jp').style.display="flex";
// });

// Opens the modal
document.querySelector('.area51').onclick = function(){
    document.querySelector('.bg-modal-jp').style.display="flex";
    document.querySelector('.swiper-replacement').style.background="linear-gradient(rgba(0,0,0,0.2),rgba(0,0,0,0.2)), url('../images/slider-1-1920x900.jpg') no-repeat scroll right center";
};

// Opens the modal
document.querySelector('.area52').onclick = function(){
    document.querySelector('.bg-modal-jp').style.display="flex";
};

// Opens the modal
document.querySelector('.area53').onclick = function(){
    document.querySelector('.bg-modal-jp').style.display="flex";
};

// Opens the modal
document.querySelector('.area54').onclick = function(){
    document.querySelector('.bg-modal-jp').style.display="flex";
};

// closes the modal
document.querySelector('.close-jp').addEventListener('click',function(){
    document.querySelector('.bg-modal-jp').style.display="none";
    document.querySelector('.swiper-replacement').style.background="url('../images/slider-1-1920x900.jpg') no-repeat scroll right center";
});


// function modalActivate(){
//     document.querySelector('.customer-button').style.display = "flex";
// };