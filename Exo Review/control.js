const PLUS_BTN = document.getElementById('plus');
PLUS_BTN.addEventListener('click', Model.addNewNote);

const CALEPIN = document.getElementById('calepin');

var Control = {
  validateNote: function(event){
    var noteId = event.target.parentNode.id;
    var noteText = event.target.parentNode.childNodes[1].value;
    Model.closeNote(noteId, noteText);
  }
};
