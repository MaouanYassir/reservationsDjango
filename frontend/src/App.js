// src/App.js
import React from 'react';
import './App.css';
import AddPriceForm from './components/AddPriceForm';  // Importer le formulaire

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Gestion des Tarifs Spéciaux</h1>
      </header>
      <main>
        <AddPriceForm />  {/* Afficher le formulaire d'ajout de tarif spécial */}
      </main>
    </div>
  );
}

export default App;

