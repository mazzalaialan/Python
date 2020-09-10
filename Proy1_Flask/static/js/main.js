
const btnDelete = document.querySelectorAll('.btn-delete')
const btnCancel= document.querySelectorAll('.btn-cancel')

if (btnDelete){
    const btnArrayD = Array.from(btnDelete)
    btnArrayD.forEach((btnD) => {
        btnD.addEventListener('click',(e) => {
            if(!confirm('Delete this Contact?')){
                e.preventDefault();
            }
        });
    });
}

if (btnCancel){
    const btnArrayC = Array.from(btnCancel)
    btnArrayC.forEach((btnC) => {
        btnC.addEventListener('click',(c) => {
            if(!confirm('Cancel the Edit?')){
                c.preventDefault();
            }
        });
    });
}