var Model = {
  notes: [],
  addNewNote: function (){
    var newNote = {
      id: Model.notes.length,
      content: ""
    };
    Model.notes.push(newNote);
    View.addNote(newNote);
  },
  closeNote: function(id, text){
    Model.notes[id].content = text;
    View.disableNote(Model.notes[id]);
  }
};
