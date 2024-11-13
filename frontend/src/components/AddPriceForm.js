import React, { useState, useEffect } from 'react';
import axios from 'axios';

function AddPriceForm() {
    const [types] = useState(['promo', 'senior', 'kids']);  // Types de tarif statiques
    const [shows, setShows] = useState([]);  // Liste des spectacles depuis Django
    const [type, setType] = useState(types[0]);
    const [price, setPrice] = useState('');
    const [showId, setShowId] = useState('');
    const [error, setError] = useState(null);
    const [success, setSuccess] = useState(null);

    useEffect(() => {
        // Récupérer la liste des spectacles depuis l'API Django
        axios.get('http://localhost:8000/catalogue/api/shows/')
            .then(response => setShows(response.data))
            .catch(error => {
                console.error("Erreur lors de la récupération des spectacles :", error);
                setError("Impossible de récupérer les spectacles.");
            });
    }, []);

    // Fonction pour soumettre le formulaire
    const handleSubmit = (event) => {
        event.preventDefault();

        // Réinitialiser les messages d'erreur et de succès
        setError(null);
        setSuccess(null);

        // Créer le payload du nouveau tarif spécial
        const newPrice = {
            type,
            price: parseFloat(price),  // Convertir le prix en nombre
            shows: [showId]  // shows prend une liste d'IDs
        };

        // Envoyer le tarif à l'API Django
        axios.post('http://localhost:8000/catalogue/api/prices/', newPrice, {
            headers: {
                // Assure-toi que l'utilisateur est authentifié et administrateur
                'Authorization': `Bearer ${localStorage.getItem('token')}`  // Utilise le token si nécessaire
            }
        })
        .then(response => {
            setSuccess("Tarif ajouté avec succès !");
            setError(null);  // Réinitialise l'erreur en cas de succès
            setPrice('');
            setShowId('');
        })
        .catch(error => {
            if (error.response && error.response.status === 403) {
                setError("Vous devez être administrateur pour ajouter un tarif spécial.");
            } else {
                setError("Une erreur est survenue lors de l'ajout du tarif.");
            }
        });
    };

    return (
        <div>
            <h2>Ajouter un Tarif Spécial</h2>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {success && <p style={{ color: 'green' }}>{success}</p>}
            <form onSubmit={handleSubmit}>
                <label>
                    Type de tarif:
                    <select value={type} onChange={(e) => setType(e.target.value)}>
                        {types.map((typeOption, index) => (
                            <option key={index} value={typeOption}>
                                {typeOption.charAt(0).toUpperCase() + typeOption.slice(1)}
                            </option>
                        ))}
                    </select>
                </label>

                <label>
                    Prix:
                    <input
                        type="number"
                        step="0.01"
                        value={price}
                        onChange={(e) => setPrice(e.target.value)}
                        required
                    />
                </label>

                <label>
                    Spectacle:
                    <select value={showId} onChange={(e) => setShowId(e.target.value)} required>
                        <option value="">Sélectionner un spectacle</option>
                        {shows.map(show => (
                            <option key={show.id} value={show.id}>
                                {show.name}
                            </option>
                        ))}
                    </select>
                </label>

                <button type="submit">Ajouter le tarif</button>
            </form>
        </div>
    );
}

export default AddPriceForm;
