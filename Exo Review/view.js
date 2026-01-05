var View = {
  addNote: function(note){
    var noteHTML = document.createElement('div');
    noteHTML.setAttribute('id', note.id);
    noteHTML.classList.add('card');
    noteHTML.classList.add('card-body');

    var title = document.createElement('h2');
    title.innerText = `#${note.id}`;
    title.classList.add('card-title');
    noteHTML.appendChild(title);

    var textA = document.createElement('textarea');
    textA.classList.add('form-control');
    textA.setAttribute('row', '5');
    noteHTML.appendChild(textA);

    var validBtn = document.createElement('div');
    validBtn.classList.add('btn');
    validBtn.classList.add('btn-success');
    validBtn.innerText = "Validate";
    validBtn.addEventListener('click', Control.validateNote);
    noteHTML.appendChild(validBtn);

    CALEPIN.appendChild(noteHTML);
  },
  disableNote: function(note){
    var noteHTML = document.getElementById(note.id);
    noteHTML.childNodes[0].classList.add('text-success');
    noteHTML.childNodes[1].remove();
    noteHTML.childNodes[1].remove();

    var noteTextp = document.createElement('p');
    noteTextp.innerText = note.content;
    noteHTML.appendChild(noteTextp);
  }
};
