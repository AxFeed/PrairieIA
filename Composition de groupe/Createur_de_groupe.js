// Liste des apprenants
let apprenantsList = [
  "Inès", "Asma", "Khrisly", "Yacine", "Ludovic",
  "Manon", "Lilian", "Manar", "Ahmadola", "Noemie", "Danitza"
];

let tableauxApprenant = []; // Contiendra les groupes
let tableau = [];           // Groupe en cours

function organisateurDeGroupe(nombreParGroupe) {
  let i = 0;

  while (apprenantsList.length !== 0) {
    // Nombre aléatoire entre 0 et length - 1
    const rnd = Math.floor(Math.random() * apprenantsList.length);

    // Ajout de l'apprenant au groupe
    tableau.push(apprenantsList[rnd]);

    // Suppression de l'apprenant pour éviter les doublons
    apprenantsList.splice(rnd, 1);

    i++;

    // Si le groupe est plein
    if (i === nombreParGroupe) {
      tableauxApprenant.push([...tableau]); // copie
      tableau.length = 0; // clear
      i = 0;
    }
  }

  // S'il reste des apprenants
  if (tableau.length !== 0) {
    tableauxApprenant.push([...tableau]);
  }

  return tableauxApprenant;
}

// Entrée utilisateur (Node.js)
const readline = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout
});

readline.question(
  "Combien voulez-vous d'apprenant par tableau ? ",
  (input) => {
    const nombreApprenantParTab = parseInt(input);

    tableauxApprenant = organisateurDeGroupe(nombreApprenantParTab);

    let i = 1;
    for (const tabApprenant of tableauxApprenant) {
      console.log(`Dans mon tableau ${i} j'ai`);
      for (const apprenant of tabApprenant) {
        console.log(apprenant);
      }
      i++;
    }

    readline.close();
  }
);
